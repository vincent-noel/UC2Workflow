import os

# Container definition for al building block of this package
CONTAINER_PATH = os.environ["COVID19_BB_IMAGES"]

MABOSS_CONTAINER = CONTAINER_PATH + "MaBoSS.sif"
PHYSIBOSS_CONTAINER = CONTAINER_PATH + "PhysiCell-COVID19.sif"
SINGLE_CELL_PROCESSING_CONTAINER = CONTAINER_PATH + "single_cell.sif"
PERSONALIZE_PATIENT_CONTAINER = CONTAINER_PATH + "PhysiCell-COVID19.sif"
META_ANALYSIS_CONTAINER = CONTAINER_PATH + "meta_analysis.sif"
