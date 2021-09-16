import os

# Container definition for al building block of this package
ASSETS_PATH = os.environ["COVID19_BB_ASSETS"]

MABOSS_ASSETS = os.path.join(ASSETS_PATH, "MaBoSS")
PHYSIBOSS_ASSETS = os.path.join(ASSETS_PATH, "PhysiBoSS")
SINGLE_CELL_PROCESSING_ASSETS = os.path.join(ASSETS_PATH, "single_cell")
PERSONALIZE_PATIENT_ASSETS = os.path.join(ASSETS_PATH, "personalize_patient")
META_ANALYSIS_ASSETS = os.path.join(ASSETS_PATH, "meta_analysis")
