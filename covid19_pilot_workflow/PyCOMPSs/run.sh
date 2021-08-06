#!/usr/bin/env bash

export COVID19_BB_IMAGES=$(pwd)/../../resources/images/
export COVID19_BB_ASSETS=$(pwd)/../../resources/assets/

dataset=$(pwd)/../../resources/data/

runcompss --log_level=debug --graph --tracing --python_interpreter=python3 covid19_pilot.py \
    ${dataset}/metadata_small.tsv \
    ${dataset}/epithelial_cell_2 \
    $(pwd)/results/ \
    $(pwd)/ko_file.txt 2 \
    epithelial_cell_2 \
    ${dataset}
