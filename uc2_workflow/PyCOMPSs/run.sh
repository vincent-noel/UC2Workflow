#!/usr/bin/env bash

export UC2_BB_IMAGES=$(pwd)/../../resources/images/
export UC2_BB_ASSETS=$(pwd)/../../resources/assets/

dataset=$(pwd)/../../resources/data/
results=$(pwd)/../../results/


runcompss --python_interpreter=python3 uc2.py \
    ${dataset}Sub_genes.csv \
    ${results}
