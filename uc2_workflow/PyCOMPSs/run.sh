#!/usr/bin/env bash

export UC2_BB_IMAGES=$(pwd)/../../resources/images/
export UC2_BB_ASSETS=$(pwd)/../../resources/assets/

dataset=$(pwd)/../../resources/data
results=$(pwd)/../../results

if [ -d "$results" ]; then
    rm -rf $results;
fi
mkdir -p $results


runcompss -d --python_interpreter=python3 uc2.py \
    ${dataset}/Sub_genes.csv \
    ${dataset}/rnaseq_fpkm_20191101.csv \
    ${dataset}/mutations_20191101.csv \
    ${dataset}/cnv_gistic_20191101.csv \
    ${dataset}/genes_druggable.csv \
    ${dataset}/genes_target.csv \
    ${results}
