import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from covid19_BBs_commons.image import SINGLE_CELL_PROCESSING_CONTAINER
from covid19_BBs_commons.assets import SINGLE_CELL_PROCESSING_ASSETS

# Globals
SINGLE_CELL_PROCESSING_BINARY = os.path.join(SINGLE_CELL_PROCESSING_ASSETS,
                                             "single_cell_processing.sh")


@container(engine="SINGULARITY", image=SINGLE_CELL_PROCESSING_CONTAINER)
@binary(binary=SINGLE_CELL_PROCESSING_BINARY)
@task(metadata=FILE_IN,
      outdir=DIRECTORY_OUT)
def single_cell_processing(metadata_flag='-m', metadata=None,
                           outdir_flag='-o', outdir=None):
    """
    Performs the Single Cell processing.

    The Definition is equal to:
        ./single_cell_processing.sh -m <metadata> -o <outdir>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the metadata file path.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    metadata = input[0]
    outdir = output[0]
    # Building block invokation
    single_cell_processing(metadata=metadata,
                           outdir=outdir)
