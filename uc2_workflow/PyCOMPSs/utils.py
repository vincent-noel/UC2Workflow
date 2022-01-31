import os
import argparse

##########################################
############ INPUT PARAMETERS ############
##########################################

def create_parser():
    """
    Create argument parser
    """
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("list_genes", type=str,
                        help="Input list of genes (.csv)")
    # parser.add_argument("profile_mutations", type=str,
    #                     help="Mutations for profile")
    # parser.add_argument("profile_cn", type=str,
    #                     help="Copy number for profile")
    # parser.add_argument("genes_drugs", type=str,
    #                     help="List of genes to simulate drugs")
    # parser.add_argument("state_objective", type=str,
    #                     help="List of genes to maximise")
    # New
    parser.add_argument("data_folder", type=str,
                        help="Data folder")
    return parser


def parse_input_parameters(show=True):
    """
    Parse input parameters
    """
    parser = create_parser()
    args = parser.parse_args()
    args.list_genes = os.path.realpath(args.list_genes)
    args.data_folder = os.path.realpath(args.data_folder)
    if show:
        print()
        print(">>> WELCOME TO THE PILOT WORKFLOW")
        print("> Parameters:")
        print("\t- list of genes file: %s" % args.list_genes)
        # print("\t- mutations file for profile: %s" % args.profile_mutations)
        # print("\t- copy number file for profile: %s" % args.profile_cn)
        # print("\t- list of genes to perturbate: %s" % args.genes_drugs)
        # print("\t- list of genes to maximise: %s" % args.state_objective)
        print("\t- data folder: %s" % args.data_folder)
        print("\n")
    return args


################################################
############ CHECK INPUT PARAMETERS ############
################################################

def check_input_parameters(args):
    """
    Check input parameters
    """
    if os.path.exists(args.data_folder):
        print("WARNING: the output folder already exists")
    else:
        os.makedirs(args.data_folder)
