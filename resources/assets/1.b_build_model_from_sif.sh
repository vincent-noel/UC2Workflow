#!/usr/bin/env bash

export UC2_BB_IMAGES=$(pwd)/../images/
export UC2_BB_ASSETS=$(pwd)/

data=$(pwd)/../data
results=$(pwd)/../../results

mkdir -p ${results}/build_model/

build_model_from_genes -d \
    -i ${data}/prova.sif \
    -o ${results}/build_model/model.bnd ${results}/build_model/model.cfg \
    -c ${data}/scenario_1_b.yml
    # --mount_point ${COVID19_BB_ASSETS}/MaBoSS:${COVID19_BB_ASSETS}/MaBoSS
