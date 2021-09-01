#!/usr/bin/python3

import os
import csv

# To set building block debug mode
from permedcoe import set_debug
# Import building block tasks
from maboss import MaBoSS_analysis
from single_cell_processing import single_cell_processing
from personalize_patient import personalize_patient
from physiboss import physiboss
from meta_analysis import meta_analysis
# Import utils
from utils import parse_input_parameters
from helpers import get_patients
from helpers import get_bnds_and_cfgs

# PyCOMPSs imports
from pycompss.api.api import compss_wait_on_directory



def main():
    """
    MAIN CODE
    """
    set_debug(False)

    print("---------------------------")
    print("| Covid-19 Pilot Workflow |")
    print("---------------------------")

    # GET INPUT PARAMETERS
    args = parse_input_parameters()

    # GENE CANDIDATES
    if os.path.exists(args.ko_file):
        print("KO file provided")
    else:
        print("KO file not detected, running MABOSS")
        ## MABOSS
        # This step produces the ko_file.txt, containing the set of selected gene candidates
        MaBoSS_analysis(args.model, args.data_folder, args.ko_file)

    # Iterate over the metadata file processing each patient
    with open(args.metadata, "r") as metadata_fd:
        reader = csv.DictReader(metadata_fd, delimiter="\t")
        out_dirs = []
        model_folders = []
        for line in reader:
            sample = line["id"]
            # SINGLE CELL PROCESSING
            print("> SINGLE CELL PROCESSING %s" % sample)
            sample_out_dir = os.path.join(args.outdir, sample)
            scp_dir = os.path.join(sample_out_dir, "single_cell_processing", "results")
            os.makedirs(scp_dir)
            scp_images_dir = os.path.join(sample_out_dir, "single_cell_processing", "images")
            os.makedirs(scp_images_dir)
            norm_data = os.path.join(scp_dir, "norm_data.tsv")
            raw_data = os.path.join(scp_dir, "raw_data.tsv")
            scaled_data = os.path.join(scp_dir, "scaled_data.tsv")
            cells_metadata = os.path.join(scp_dir, "cells_metadata.tsv")
            if line["file"].startswith("../.."):
                # Two folder relative
                relative_p_file = os.path.join(*(line["file"].split(os.path.sep)[2:]))  # remove first two folders "../.."
                p_file = os.path.join("..", "..", "resources", relative_p_file)
            else:
                # Absolute path
                p_file = line["file"]
            single_cell_processing(p_id=sample,
                                   p_group=line["group"],
                                   p_file=p_file,
                                   norm_data=norm_data,
                                   raw_data=raw_data,
                                   scaled_data=scaled_data,
                                   cells_metadata=cells_metadata,
                                   outdir=scp_images_dir)

            # PERSONALIZE PATIENT
            print("> PERSONALIZING PATIENT %s" % sample)
            pp_dir = os.path.join(sample_out_dir, "personalize_patient")
            model_output_dir = os.path.join(pp_dir, "models")
            os.makedirs(pp_dir)
            model_folders.append(model_output_dir)
            personalized_result = os.path.join(pp_dir, "personalized_by_cell_type.tsv")
            out_dirs.append((sample, model_output_dir))
            personalize_patient(norm_data=norm_data,
                                cells=cells_metadata,
                                model_prefix=args.model_prefix,
                                t="Epithelial_cells",
                                model_output_dir=model_output_dir,
                                personalized_result=personalized_result,
                                ko=args.ko_file)

    # Wait for all personalization
    # Currently needed because each personalization is written within args.outdir
    # and we need to know how many bnds are inside (Depends on the number of ko)
    for _, model_folder in out_dirs:
        compss_wait_on_directory(model_folder)

    physiboss_results = []
    physiboss_subfolder = "physiboss_results"  # do not modify (hardcoded in meta-analysis)
    for sample, model_folder in out_dirs:
        bnds_and_cfgs = get_bnds_and_cfgs(model_folder)
        for prefix, bnd, cfg in bnds_and_cfgs:
            print(">> prefix: " + str(prefix))
            print(">> bnd: " + str(bnd))
            print(">> cfg: " + str(cfg))
            for r in range(1, args.reps + 1):
                print(">>> Repetition: " + str(r))
                name = "output_" + sample + "_" + prefix + "_" + str(r)
                out_name = name + ".out"
                out_file = os.path.join(args.outdir, sample, physiboss_subfolder, out_name)
                err_name = name + ".err"
                err_file = os.path.join(args.outdir, sample, physiboss_subfolder, err_name)
                print("\t- " + out_file)
                print("\t- " + err_file)
                results_dir = os.path.join(args.outdir, sample, physiboss_subfolder, prefix + "_physiboss_run_" + str(r))
                os.makedirs(results_dir)
                physiboss_results.append(results_dir)
                physiboss(sample=sample,
                            repetition=r,
                            prefix=prefix,
                            bnd_file=bnd,
                            cfg_file=cfg,
                            out_file=out_file,
                            err_file=err_file,
                            results_dir=results_dir)

    # Wait for all physiboss
    # Currently needed because the meta analysis requires all of them
    # and its input is the main folder. It assumes the internal folder
    # structure
    for physiboss_result in physiboss_results:
        compss_wait_on_directory(physiboss_result)

    # Perform last step: meta analysis
    final_result_dir = os.path.join(args.outdir, "meta_analysis")
    os.makedirs(final_result_dir)
    meta_analysis(meta_file=args.metadata,
                  out_dir=args.outdir,
                  model_prefix=args.model,
                  ko_file=args.ko_file,
                  reps=args.reps,
                  verbose="T",
                  results=final_result_dir)


if __name__ == "__main__":
    main()
