#!/usr/bin/env bash

export COMPSS_PYTHON_VERSION=3-ML
module load COMPSs/2.10.pr
module load singularity/3.5.2
module use /apps/modules/modulefiles/tools/COMPSs/libraries
module load permedcoe  # generic permedcoe package

# Override the following for using different images, assets or dataset
export COVID19_BB_IMAGES=${COVID19_BB_IMAGES}  # Currently using the "permedcoe" deployed
export COVID19_BB_ASSETS=${COVID19_BB_ASSETS}  # Currently using the "permedcoe" deployed
dataset=${COVID19_PILOT_DATASET}               # Currently using the "permedcoe" deployed

enqueue_compss \
    --num_nodes=2 \
    --exec_time=45 \
    --worker_working_dir=$(pwd) \
    --log_level=off \
    --graph \
    --tracing \
    --python_interpreter=python3 \
    covid19_pilot.py \
        ${dataset}metadata_clean.tsv \
        ${dataset}epithelial_cell_2 \
        $(pwd)/results/ \
        $(pwd)/ko_file.txt \
        2 \
        epithelial_cell_2 \
        ${dataset}

######################################################
# APPLICATION EXECUTION EXAMPLE
# Call:
#       ./launch.sh
#
# Example:
#       ./launch.sh
######################################################
