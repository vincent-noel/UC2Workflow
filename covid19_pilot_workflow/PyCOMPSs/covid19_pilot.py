#!/usr/bin/python3

import os

# To set building block debug mode
from permedcoe import set_debug
# Import building block tasks
from maboss import MaBoSS_analysis
from single_cell_processing import single_cell_processing
from personalize_patient import personalize_patient
from physiboss import physiboss
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
        ## MABOSS BUILDING BLOCK
        # This step produces the ko_file.txt, containing the set of selected gene candidates
        MaBoSS_analysis(args.model, args.data_folder, args.ko_file)

    # SINGLE CELL PROCESSING
    ## SINGLE-CELL PROCESSING BUILDING BLOCK
    single_cell_processing(metadata=args.metadata,
                           outdir=args.outdir)

    # wait until all single cell have been produced because we need to iterate
    # over the bnd files within outdir
    compss_wait_on_directory(args.outdir)

    # RUN BY PATIENT
    patients_id = get_patients(args.metadata)
    out_dirs = []
    for sample in patients_id:
        print("> PERSONALIZING PATIENT %s" % sample)

        ## PERSONALIZE PATIENT BUILDING BLOCK
        norm_data = os.path.join(args.outdir, sample, "norm_data.tsv")
        cells_metadata = os.path.join(args.outdir, sample, "cells_metadata.tsv")
        output_dir = os.path.join(args.outdir, sample)
        out_dirs.append(output_dir)
        personalize_patient(norm_data=norm_data,
                            cells=cells_metadata,
                            model_prefix=args.model_prefix,
                            t="Epithelial_cells",
                            output_dir=output_dir,
                            ko=args.ko_file)

    # wait until each patient outdir
    # Currently needed because each personalization is written within args.outdir
    for i in range(len(out_dirs)):
        compss_wait_on_directory(out_dirs[i])

    for sample in patients_id:
        bnds_and_cfgs = get_bnds_and_cfgs(args.outdir, sample)
        for prefix, bnd, cfg in bnds_and_cfgs:
            print(">> prefix: " + str(prefix))
            print(">> bnd: " + str(bnd))
            print(">> cfg: " + str(cfg))
            for r in range(args.reps):
                print(">>> Repetition: " + str(r))
                name = "output_" + sample + "_" + prefix + "_" + str(r)
                out_name = name + ".out"
                out_file = os.path.join(args.outdir, sample, out_name)
                err_name = name + ".err"
                err_file = os.path.join(args.outdir, sample, err_name)
                print("\t- " + out_file)
                print("\t- " + err_file)
                physiboss(sample=sample,
                          repetition=r,
                          prefix=prefix,
                          bnd_file=bnd,
                          cfg_file=cfg,
                          out_file=out_file,
                          err_file=err_file)


if __name__ == "__main__":
    main()
