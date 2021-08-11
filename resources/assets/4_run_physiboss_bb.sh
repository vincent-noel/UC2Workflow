#!/usr/bin/env bash

export COVID19_BB_IMAGES=$(pwd)/../images/
export COVID19_BB_ASSETS=$(pwd)/

# Just one sample call for C141
physiboss -d \
    -i C141 1 epithelial_cell_2_personalized \
       $(pwd)/result/C141/personalize_patient/models/epithelial_cell_2_personalized.bnd \
       $(pwd)/result/C141/personalize_patient/models/epithelial_cell_2_personalized.cfg \
    -o $(pwd)/result/C141/output_C141_epithelial_cell_2_personalized_0.out \
       $(pwd)/result/C141/output_C141_epithelial_cell_2_personalized_0.err \
    --mount_points ${COVID19_BB_ASSETS}/PhysiBoSS/:${COVID19_BB_ASSETS}/PhysiBoSS/
