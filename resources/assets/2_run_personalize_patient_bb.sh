#!/usr/bin/env bash

export UC2_BB_IMAGES=$(pwd)/../images/
export UC2_BB_ASSETS=$(pwd)/

data=$(pwd)/../data
results=$(pwd)/../../results
mod_results=${results}/build_model
per_results=${results}/personalize_patient

# Data is too big for github, so I compressed it. Need to uncompress first
tar -zxvf ${data}/data_celllines.tar.gz --directory ${data}

# 1st cell line
cell_line=SIDM00003
mkdir -p ${per_results}/${cell_line}/

personalize_patient -d \
    -i ${data}/rnaseq_fpkm_20191101.csv \
       ${data}/mutations_20191101.csv.csv \
       ${data}/cnv_gistic_20191101.csv \
       ${cell_line} \
       ${mod_results}/model.bnd \
       ${mod_results}/model.cfg \
    -o ${per_results}/${cell_line}/ \
    -c ${data}/personalization.yml \
    --mount_points ${UC2_BB_ASSETS}/personalize_patient/:${UC2_BB_ASSETS}/personalize_patient/,$(pwd)/../data/:$(pwd)/../data/

# 2nd cell line

cell_line=SIDM00023

mkdir -p ${per_results}/${cell_line}/

personalize_patient -d \
    -i ${data}/rnaseq_fpkm_20191101.csv \
       ${data}/mutations_20191101.csv.csv \
       ${data}/cnv_gistic_20191101.csv \
       ${cell_line} \
       ${mod_results}/model.bnd \
       ${mod_results}/model.cfg \
    -o ${per_results}/${cell_line}/ \
    -c ${data}/personalization.yml \
    --mount_points ${UC2_BB_ASSETS}/personalize_patient/:${UC2_BB_ASSETS}/personalize_patient/,$(pwd)/../data/:$(pwd)/../data/


# 3rd cell line

cell_line=SIDM00040

mkdir -p ${per_results}/${cell_line}/

personalize_patient -d \
    -i ${data}/rnaseq_fpkm_20191101.csv \
       ${data}/mutations_20191101.csv.csv \
       ${data}/cnv_gistic_20191101.csv \
       ${cell_line} \
       ${mod_results}/model.bnd \
       ${mod_results}/model.cfg \
    -o ${per_results}/${cell_line}/ \
    -c ${data}/personalization.yml \
    --mount_points ${UC2_BB_ASSETS}/personalize_patient/:${UC2_BB_ASSETS}/personalize_patient/,$(pwd)/../data/:$(pwd)/../data/
