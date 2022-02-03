#!/usr/bin/python3

import os

# To set building block debug mode
from permedcoe import set_debug
# Import building block tasks
from build_model_from_genes import build_model_from_species
from personalize_patient import personalize_patient
from personalize_patient import personalize_patient_cellline
from maboss_bb import MaBoSS_analysis
from maboss_bb import MaBoSS_sensitivity_analysis
from print_drug_results import print_drug_results
# Import utils
from utils import parse_input_parameters
from helpers import get_genefiles

# PyCOMPSs imports
from pycompss.api.api import compss_wait_on_directory
from pycompss.api.api import compss_wait_on_file
from pycompss.api.api import compss_barrier

def main():
    """
    MAIN CODE
    """
    set_debug(True)

    print("---------------------------")
    print("|   Use Case 2 Workflow   |")
    print("---------------------------")

    # GET INPUT PARAMETERS
    args = parse_input_parameters()

    if not os.path.exists(args.results_folder):
        os.makedirs(args.results_folder, exist_ok=True)

    # 1st STEP: Build model from species
    build_model_folder = os.path.join(args.results_folder, "build_model")
    os.makedirs(build_model_folder, exist_ok=True)
    model_bnd_path = os.path.join(build_model_folder, "model.bnd")
    model_cfg_path = os.path.join(build_model_folder, "model.cfg")

    build_model_from_species(
        input_file=args.list_genes,
        output_bnd_file=model_bnd_path,
        output_cfg_file=model_cfg_path
    )

    cell_lines = ["SIDM00003", "SIDM00023", "SIDM00040"]  # TODO: get this list from cnv_gistic_20191101.csv
    personalize_patient_folder = os.path.join(args.results_folder, "personalize_patient")
    os.makedirs(personalize_patient_folder, exist_ok=True)
    mutant_results_folder = os.path.join(args.results_folder, "mutant_results")
    os.makedirs(mutant_results_folder, exist_ok=True)
    for cell_line in cell_lines:

        # 2nd STEP: Personalize patients
        personalize_patient_folder_cell = os.path.join(personalize_patient_folder, cell_line)
        os.makedirs(personalize_patient_folder_cell, exist_ok=True)
        personalize_patient_cellline(
            expression_data=args.rnaseq_data,
            cnv_data=args.cn_data,
            mutation_data=args.mutation_data,
            model_bnd=model_bnd_path,
            model_cfg=model_cfg_path,
            t=cell_line,
            model_output_dir=personalize_patient_folder_cell
        )

        # 3rd STEP: MaBoSS
        mutant_results_folder_cell = os.path.join(mutant_results_folder, cell_line)
        os.makedirs(mutant_results_folder_cell, exist_ok=True)
        MaBoSS_sensitivity_analysis(
            model_folder=personalize_patient_folder_cell,
            genes_druggable=args.genes_drugs,
            genes_target=args.state_objective,
            result_folder=mutant_results_folder_cell
        )

    compss_barrier()


if __name__ == "__main__":
    main()
