#!/usr/bin/env bash

export COVID19_BB_IMAGES=$(pwd)/../images/
export COVID19_BB_ASSETS=$(pwd)/

# Just one sample call for C141
personalize_patient -d \
    -i $(pwd)/result/C141/norm_data.tsv $(pwd)/result/C141/cells_metadata.tsv $(pwd)/../data/epithelial_cell_2 Epithelial_cells $(pwd)/ko_file.txt \
    -o $(pwd)/result/C141/ \
    --mount_points ${COVID19_BB_ASSETS}/personalize_patient/:${COVID19_BB_ASSETS}/personalize_patient/,$(pwd)/../data/:$(pwd)/../data/
