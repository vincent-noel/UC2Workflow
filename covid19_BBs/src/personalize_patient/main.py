import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_INOUT

# Import single container and assets definitions
from covid19_BBs_commons.image import PERSONALIZE_PATIENT_CONTAINER
from covid19_BBs_commons.assets import PERSONALIZE_PATIENT_ASSETS

# Globals
PERSONALIZE_PATIENT_BINARY = os.path.join(PERSONALIZE_PATIENT_ASSETS,
                                          "personalize_patient.sh")


@container(engine="SINGULARITY", image=PERSONALIZE_PATIENT_CONTAINER)
@binary(binary=PERSONALIZE_PATIENT_BINARY)
@task(norm_data=FILE_IN, cells=FILE_IN, output_dir=DIRECTORY_INOUT, ko=FILE_IN)
def personalize_patient(norm_data_flag="-e", norm_data=None,
                        cells_flag="-c", cells=None,
                        model_prefix_flag="-m", model_prefix="prefix",
                        t_flag="-t", t="Epithelial_cells",
                        output_flag="-o", output_dir=None,
                        ko_flag="-k", ko=None,
                        ):
    """
    Performs the personalize patient.

    The Definition is equal to:
       ./personalize_patient.sh \
       -e <norm_data> \
       -c <cells> \
       -m <model_prefix> -t <t> \
       -o <output_dir> -k <ko>
    Sample:
       ./personalize_patient.sh \
       -e $outdir/$sample/norm_data.tsv \
       -c $outdir/$sample/cells_metadata.tsv \
       -m $model_prefix -t Epithelial_cells \
       -o $outdir/$sample -k $ko_file
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
    norm_data = input[0]
    cells = input[1]
    model_prefix = input[2]
    t = input[3]
    ko = input[4]
    output = output[0]
    # Building block invokation
    personalize_patient(norm_data=norm_data,
                        cells=cells,
                        model_prefix=model_prefix,
                        t=t,
                        output_dir=output,
                        ko=ko)
