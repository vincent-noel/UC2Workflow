import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from uc2_BBs_commons.image import MABOSS_CONTAINER
from uc2_BBs_commons.assets import PRINT_DRUG_RESULTS_ASSETS

# Globals
PRINT_DRUG_RESULTS_BINARY = os.path.join(PRINT_DRUG_RESULTS_ASSETS,
                                          "print_result_drugs.sh")


@container(engine="SINGULARITY", image=MABOSS_CONTAINER)
@binary(binary=PRINT_DRUG_RESULTS_BINARY)
@task(drug_results_folder=DIRECTORY_IN, reports_folder=DIRECTORY_OUT)
def print_drug_results(drug_results_folder=None, reports_folder=None):
    """
    
    """
    # Empty function since it represents a binary execution:
    pass

def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the normalized data file path, cells
                      metadata, model prefix, tag and ko file.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    
    # Process parameters
    results_folder = input[0]
    reports_folder = output[0]
    # Building block invocation
    print_drug_results(
        drug_results_folder=results_folder, 
        reports_folder=reports_folder
    )