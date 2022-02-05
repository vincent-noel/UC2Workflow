#!/usr/bin/env bash
export UC2_BB_IMAGES=$(pwd)/../images/
export UC2_BB_ASSETS=$(pwd)/

data=$(pwd)/../data
results=$(pwd)/../../results
per_results=${results}/personalize_patient
mut_results=${results}/mutant_results


# 1st patient

mkdir -p ${mut_results}/SIDM00003

maboss_bb -d \
    -i ${per_results}/SIDM00003/ \
       ${data}/genes_druggable.csv \
       ${data}/genes_target.csv \
    -o ${mut_results}/SIDM00003/sensitivity.json \
    -c ${data}/personalization.yml \
    --mount_points ${UC2_BB_ASSETS}/MaBoSS_BB/:${UC2_BB_ASSETS}/MaBoSS_BB/

mkdir -p ${mut_results}/SIDM00023

maboss_bb -d \
    -i ${per_results}/SIDM00023/ \
       ${data}/genes_druggable.csv \
       ${data}/genes_target.csv \
    -o ${mut_results}/SIDM00023/sensitivity.json \
    -c ${data}/personalization.yml \
    --mount_points ${UC2_BB_ASSETS}/MaBoSS_BB/:${UC2_BB_ASSETS}/MaBoSS_BB/

mkdir -p ${mut_results}/SIDM00040

maboss_bb -d \
    -i ${per_results}/SIDM00040/ \
       ${data}/genes_druggable.csv \
       ${data}/genes_target.csv \
    -o ${mut_results}/SIDM00040/sensitivity.json \
    -c ${data}/personalization.yml \
    --mount_points ${UC2_BB_ASSETS}/MaBoSS_BB/:${UC2_BB_ASSETS}/MaBoSS_BB/
