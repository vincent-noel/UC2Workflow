#!/usr/bin/env bash

export COVID19_BB_IMAGES=$(pwd)/../images/
export COVID19_BB_ASSETS=$(pwd)/

single_cell_processing -d \
    -i $(pwd)/../data/metadata_small.tsv \
    -o $(pwd)/result \
    --mount_points ${COVID19_BB_ASSETS}/single_cell/:${COVID19_BB_ASSETS}/single_cell/
