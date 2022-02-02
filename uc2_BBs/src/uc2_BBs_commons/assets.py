import os

# Container definition for al building block of this package
ASSETS_PATH = os.environ["UC2_BB_ASSETS"]

PRINT_DRUG_RESULTS_ASSETS = os.path.join(ASSETS_PATH, "print_result_drugs")
MABOSS_ASSETS = os.path.join(ASSETS_PATH, "MaBoSS_BB")
PHYSIBOSS_ASSETS = os.path.join(ASSETS_PATH, "PhysiBoSS")
SINGLE_CELL_PROCESSING_ASSETS = os.path.join(ASSETS_PATH, "single_cell")
PERSONALIZE_PATIENT_ASSETS = os.path.join(ASSETS_PATH, "personalize_patient")
META_ANALYSIS_ASSETS = os.path.join(ASSETS_PATH, "meta_analysis")
