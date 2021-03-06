import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container and assets definitions
from uc2_BBs_commons.image import MABOSS_CONTAINER
from uc2_BBs_commons.assets import MABOSS_ASSETS

# Globals
MABOSS_BINARY = os.path.join(MABOSS_ASSETS, "MaBoSS_analysis.sh")
MABOSS_SENSITIVIY_ANALYSIS = os.path.join(MABOSS_ASSETS, "MaBoSS_sensitivity_analysis.sh")


@container(engine="SINGULARITY", image=MABOSS_CONTAINER)
@binary(binary=MABOSS_BINARY)
@task(data_folder=DIRECTORY_IN, ko_file=FILE_OUT)
def MaBoSS_analysis(model="epithelial_cell_2",
                    data_folder=None,
                    ko_file=None):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_analysis.sh <model> <data_folder> <ko_file>
    """
    # Empty function since it represents a binary execution:
    pass


@container(engine="SINGULARITY", image=MABOSS_CONTAINER)
@binary(binary=MABOSS_SENSITIVIY_ANALYSIS)
@task(model_folder=DIRECTORY_IN, genes_druggable=FILE_IN, genes_target=FILE_IN, result_file=FILE_OUT)
def MaBoSS_sensitivity_analysis(model_folder=None,
                                genes_druggable=None,
                                genes_target=None,
                                result_file=None):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_analysis.sh <model> <data_folder> <ko_file>
    """
    # Empty function since it represents a binary execution:
    pass



def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the model and data folder.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """

    if ("uc2" in config.keys() and config["uc2"]):
        # Process parameters
        model_folder = input[0]
        genes_druggable = input[1]
        genes_target = input[2]
        result_file = output[0]
        # Building block invokation
        MaBoSS_sensitivity_analysis(model_folder=model_folder,
                        genes_druggable=genes_druggable,
                        genes_target=genes_target,
                        result_file=result_file)

    else:
        # Process parameters
        model_folder = input[0]
        data_folder = input[1]
        ko_file = output[0]
        # Building block invokation
        MaBoSS_analysis(model=model,
                        data_folder=data_folder,
                        ko_file=ko_file)
