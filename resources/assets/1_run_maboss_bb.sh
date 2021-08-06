#!/usr/bin/env bash

export COVID19_BB_IMAGES=$(pwd)/../images/
export COVID19_BB_ASSETS=$(pwd)/

maboss -d \
    -i epithelial_cell_2 $(pwd)/../data \
    -o $(pwd)/ko_file.txt \
    --mount_point ${COVID19_BB_ASSETS}/MaBoSS:${COVID19_BB_ASSETS}/MaBoSS
