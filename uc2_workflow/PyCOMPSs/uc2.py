#!/usr/bin/python3

import os
import csv
from re import A

# To set building block debug mode
from permedcoe import set_debug
from permedcoe.utils.log import LOG_LEVEL_DEBUG, init_logging
# Import building block tasks
from build_model_from_genes import build_model_from_species
from maboss_bb import MaBoSS_analysis
# from single_cell_processing import single_cell_processing
from personalize_patient import personalize_patient, personalize_patient_cellline
# from physiboss import physiboss_model
# from meta_analysis import meta_analysis
# Import utils
from utils import parse_input_parameters
from helpers import get_genefiles

# PyCOMPSs imports
from pycompss.api.api import compss_wait_on_directory
from pycompss.api.api import compss_wait_on_file

def main():
    """
    MAIN CODE
    """
    set_debug(True)
    # init_logging(True)
    
    print("---------------------------")
    print("|   Use Case 2 Workflow   |")
    print("---------------------------")

    # GET INPUT PARAMETERS
    args = parse_input_parameters()

    if not os.path.exists(args.data_folder):
        os.makedirs(args.data_folder, exist_ok=True)

    # GENE CANDIDATES
    if os.path.exists(args.list_genes):
        print("List of genes file provided")
        
        os.makedirs(os.path.join(args.data_folder, "build_model"), exist_ok=True)
        model_bnd_path = os.path.join(args.data_folder, "build_model", "model.bnd")
        model_cfg_path = os.path.join(args.data_folder, "build_model", "model.cfg")

        build_model_from_species(
            input_file=args.list_genes, 
            output_bnd_file=model_bnd_path, 
            output_cfg_file=model_cfg_path
        )

        compss_wait_on_file(model_bnd_path)
        compss_wait_on_file(model_cfg_path)

        os.makedirs(os.path.join(args.data_folder, "personalize_patient"), exist_ok=True)
        os.makedirs(os.path.join(args.data_folder, "personalize_patient", "SIDM00003"), exist_ok=True)

        personalize_patient_cellline(expression_data=args.rnaseq_data,
                cnv_data=args.cn_data, mutation_data=args.mutation_data,
                model_prefix=os.path.dirname(model_bnd_path), t="SIDM00003",
                model_output_dir=os.path.join(args.data_folder, "personalize_patient", "SIDM00003")
                # personalized_result=os.path.join(args.data_folder, "personalize_patient", "SIDM00003", "personalized_by_celltype.tsv"),
        )
        
        compss_wait_on_file(model_bnd_path)


    # # Discover gene candidates
    # genes = [""]  # first empty since it is the original without gene ko
    # with open(args.ko_file, "r") as ko_fd:
    #     genes += ko_fd.read().splitlines()
    # genefiles = get_genefiles(args.model, genes)

    # # Iterate over the metadata file processing each patient
    # physiboss_results = []
    # physiboss_subfolder = "physiboss_results"  # do not modify (hardcoded in meta-analysis)
    # with open(args.metadata, "r") as metadata_fd:
    #     reader = csv.DictReader(metadata_fd, delimiter="\t")
    #     for line in reader:
    #         # ONE LINE PER PATIENT
    #         sample = line["id"]
    #         # SINGLE CELL PROCESSING
    #         print("> SINGLE CELL PROCESSING %s" % sample)
    #         sample_out_dir = os.path.join(args.outdir, sample)
    #         scp_dir = os.path.join(sample_out_dir, "single_cell_processing", "results")
    #         os.makedirs(scp_dir)
    #         scp_images_dir = os.path.join(sample_out_dir, "single_cell_processing", "images")
    #         os.makedirs(scp_images_dir)
    #         norm_data = os.path.join(scp_dir, "norm_data.tsv")
    #         raw_data = os.path.join(scp_dir, "raw_data.tsv")
    #         scaled_data = os.path.join(scp_dir, "scaled_data.tsv")
    #         cells_metadata = os.path.join(scp_dir, "cells_metadata.tsv")
    #         if line["file"].startswith("../.."):
    #             # Two folder relative - Local
    #             relative_p_file = os.path.join(*(line["file"].split(os.path.sep)[2:]))  # remove first two folders "../.."
    #             p_file = os.path.join("..", "..", "resources", relative_p_file)
    #         else:
    #             # Absolute path - Supercomputer
    #             p_file = line["file"]
    #         single_cell_processing(p_id=sample,
    #                                p_group=line["group"],
    #                                p_file=p_file,
    #                                norm_data=norm_data,
    #                                raw_data=raw_data,
    #                                scaled_data=scaled_data,
    #                                cells_metadata=cells_metadata,
    #                                outdir=scp_images_dir)

    #         # PERSONALIZE PATIENT
    #         print("> PERSONALIZING PATIENT %s" % sample)
    #         pp_dir = os.path.join(sample_out_dir, "personalize_patient")
    #         os.makedirs(pp_dir)
    #         model_output_dir = os.path.join(pp_dir, "models")
    #         personalized_result = os.path.join(pp_dir, "personalized_by_cell_type.tsv")
    #         personalize_patient(norm_data=norm_data,
    #                             cells=cells_metadata,
    #                             model_prefix=args.model_prefix,
    #                             t="Epithelial_cells",
    #                             model_output_dir=model_output_dir,
    #                             personalized_result=personalized_result,
    #                             ko=args.ko_file)

    #         for gene_prefix in genefiles:
    #             print(">> prefix: " + str(gene_prefix))
    #             for r in range(1, args.reps + 1):
    #                 print(">>> Repetition: " + str(r))
    #                 name = "output_" + sample + "_" + gene_prefix + "_" + str(r)
    #                 out_file = os.path.join(args.outdir, sample, physiboss_subfolder, name + ".out")
    #                 err_file = os.path.join(args.outdir, sample, physiboss_subfolder, name + ".err")
    #                 print("\t- " + out_file)
    #                 print("\t- " + err_file)
    #                 results_dir = os.path.join(args.outdir, sample, physiboss_subfolder, gene_prefix + "_physiboss_run_" + str(r))
    #                 os.makedirs(results_dir)
    #                 physiboss_results.append(results_dir)
    #                 # PHYSIBOSS
    #                 physiboss_model(sample=sample,
    #                                 repetition=r,
    #                                 prefix=gene_prefix,
    #                                 model_dir=model_output_dir,
    #                                 out_file=out_file,
    #                                 err_file=err_file,
    #                                 results_dir=results_dir)

    # # Wait for all physiboss
    # # Currently needed because the meta analysis requires all of them
    # # and its input is the main folder. It assumes the internal folder
    # # structure
    # for physiboss_result in physiboss_results:
    #     compss_wait_on_directory(physiboss_result)

    # # Perform last step: meta analysis
    # final_result_dir = os.path.join(args.outdir, "meta_analysis")
    # os.makedirs(final_result_dir)
    # # META-ANALYSIS
    # meta_analysis(meta_file=args.metadata,
    #               out_dir=args.outdir,
    #               model_prefix=args.model,
    #               ko_file=args.ko_file,
    #               reps=args.reps,
    #               verbose="T",
    #               results=final_result_dir)


if __name__ == "__main__":
    main()
