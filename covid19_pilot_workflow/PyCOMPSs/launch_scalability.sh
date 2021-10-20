#!/usr/bin/env bash

export COMPSS_PYTHON_VERSION=3-ML
#module load COMPSs/2.9
module use /apps/modules/modulefiles/tools/COMPSs/.custom
module load TrunkJCB_permedcoe
module load singularity/3.5.2
module use /apps/modules/modulefiles/tools/COMPSs/libraries
module load permedcoe_scalability  # generic permedcoe package

# Override the following for using different images, assets or dataset
export COVID19_BB_IMAGES=${COVID19_BB_IMAGES}  # Currently using the "permedcoe" deployed
export COVID19_BB_ASSETS=${COVID19_BB_ASSETS}  # Currently using the "permedcoe" deployed
dataset=${COVID19_PILOT_DATASET}               # Currently using the "permedcoe" deployed


# Set the tool internal parallelism and constraint
export COMPUTING_UNITS=1

enqueue_compss \
    --num_nodes=2 \
    --exec_time=15 \
    --worker_working_dir=$(pwd) \
    --log_level=off \
    --graph \
    --tracing \
    --python_interpreter=python3 \
    covid19_pilot.py \
        ${dataset}metadata_one.tsv \
        ${dataset}epithelial_cell_2 \
        $(pwd)/results_${COMPUTING_UNITS}/ \
        $(pwd)/ko_file.txt \
        1 \
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