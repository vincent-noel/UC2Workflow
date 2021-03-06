import os

# Container definition for al building block of this package
CONTAINER_PATH = os.environ["UC2_BB_IMAGES"]

FROM_SPECIES_TO_MABOSS_MODEL_CONTAINER = CONTAINER_PATH + "FromSpeciesToMaBoSSModel.sif"
MABOSS_CONTAINER = CONTAINER_PATH + "MaBoSS.sif"
SINGLE_CELL_PROCESSING_CONTAINER = CONTAINER_PATH + "single_cell.sif"
PERSONALIZE_PATIENT_CONTAINER = CONTAINER_PATH + "PhysiCell-COVID19.sif"
META_ANALYSIS_CONTAINER = CONTAINER_PATH + "meta_analysis.sif"
PRINT_DRUG_RESULTS_CONTAINER = CONTAINER_PATH + "printResults.sif"
