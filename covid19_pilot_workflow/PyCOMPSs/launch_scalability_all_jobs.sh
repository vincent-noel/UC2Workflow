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


# Set the tool internal parallelism and constraint
export COMPUTING_UNITS=1
id=$(./launch_scalability_job.sh None | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

export COMPUTING_UNITS=2
id=$(./launch_scalability_job.sh $id | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

export COMPUTING_UNITS=4
id=$(./launch_scalability_job.sh $id | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

export COMPUTING_UNITS=8
id=$(./launch_scalability_job.sh $id | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

export COMPUTING_UNITS=16
id=$(./launch_scalability_job.sh $id | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

export COMPUTING_UNITS=32
id=$(./launch_scalability_job.sh $id | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

export COMPUTING_UNITS=48
id=$(./launch_scalability_job.sh $id | grep "Submitted batch job" | cut -d " " -f 4)
echo $id

