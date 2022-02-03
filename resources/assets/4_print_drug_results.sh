#!/usr/bin/env bash
export UC2_BB_IMAGES=$(pwd)/../images/
export UC2_BB_ASSETS=$(pwd)/

data=$(pwd)/../data
results=$(pwd)/../../results
mut_results=${results}/mutant_results
rep_results=${results}/report

# 1st patient
mkdir -p ${rep_results}

print_drug_results -d \
    -i ${mut_results} \
    -o ${rep_results} \
    --mount_points ${UC2_BB_ASSETS}print_result_drugs/:${UC2_BB_ASSETS}print_result_drugs/
