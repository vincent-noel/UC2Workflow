import os
import glob
from pathlib import Path

def get_patients(metadata):
    """
    Parse the "metadata" file and get the patients
    """
    with open(metadata, 'r') as metadata_fd:
        metadata_content = metadata_fd.readlines()
    # Clean whitespaces begin and end
    metadata_content = [line.strip() for line in metadata_content]
    # Remove header
    metadata_content = metadata_content[1:]
    # Parse lines
    parsed_metadata = []
    for line in metadata_content:
        elements = line.split()
        parsed_metadata.append(elements)
    # Filter patients
    patients_id = [patient[0] for patient in parsed_metadata]
    return patients_id


def get_bnds_and_cfgs(outdir, sample):
    """
    Create a list of bnd files for the given patient.
    # bnd_files = os.path.join(outdir/$sample/models/*bnd)

    :param outdir: Single cell output directory
    :param sample: Patient id
    :return: List of triplets with name, bnd and cfv files associated to the patient id
    """
    path = os.path.join(outdir, sample, "models")
    bnd_extension = "/*.bnd"
    bnd_files = glob.glob(path + bnd_extension)
    bnds_and_cfgs = []
    for bnd_f in bnd_files:
        bnd_f_p = Path(bnd_f)
        name = str(bnd_f_p.stem)
        cfg_f = str(bnd_f_p.with_suffix(".cfg"))
        bnds_and_cfgs.append((name, bnd_f, cfg_f))
    return bnds_and_cfgs
