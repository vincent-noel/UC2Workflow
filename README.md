# Use Case 2 Workflow

This folder contains all needed for the Use Case 2 Workflow : Drug synergies on cell lines.

- [Use Case 2 Workflow](#use-case-2-workflow)
  - [Contents](#contents)
    - [Building Blocks](#building-blocks)
    - [Workflows](#workflows)
    - [Resources](#resources)
  - [Instructions](#instructions)
    - [Local machine](#local-machine)
      - [Requirements](#requirements)
      - [Usage steps](#usage-steps)
    - [MareNostrum 4](#marenostrum-4)
      - [Requirements in MN4](#requirements-in-mn4)
      - [Usage steps in MN4](#usage-steps-in-mn4)
  - [License](#license)
  - [Contact](#contact)

## Contents

### Building Blocks

The ``uc2_BBs`` folder contains the Building Blocks used in the UC2 Workflow.

### Workflows

The ``uc2_workflow`` folder contains the workflows implementations.

Currently contains only the implementation using PyCOMPSs.

### Resources

The ``resources`` folder contains the building blocks assets and images, and
a small dataset.

## Instructions

### Local machine

This section explains the requirements and usage for the COVID19 Pilot workflow in a laptop or desktop computer.

#### Requirements

- [`permedcoe`](https://github.com/PerMedCoE/permedcoe) package
- [PyCOMPSs](https://pycompss.readthedocs.io/en/stable/Sections/00_Quickstart.html#install-compss)
- [Singularity](https://sylabs.io/guides/3.0/user-guide/installation.html)

#### Usage steps

1. Clone this repository
2. Install the `uc2_BBs` package

   ```bash
   cd covid19_BBs && ./install.sh && cd ..
   ```

3. Go to `uc2_workflow/PyCOMPSs` folder
4. Execute `./run.sh`

The execution is prepared to use the singularity images that **must** be placed into `resources/images` folder (`MaBoSS.sif`, `PhysiCell-COVID19.sif` and `single_cell.sif`), the assets folder located into `resources/assets` and the dataset located into `resources/data`.

> :warning: **WARNING**: The singularity containers **need to be downloaded** from the project [B2DROP](https://b2drop.bsc.es/index.php/f/444350).

> **TIP**: If you want to run the workflow with a different dataset, please place the dataset into `resources/data` and update the `run.sh` script according to the dataset name.

### MareNostrum 4

This section explains the requirements and usage for the COVID19 Pilot workflow in the MareNostrum 4 supercomputer.

#### Requirements in MN4

- Access to MN4

All requirements are already installed in MN4.

#### Usage steps in MN4

1. Load the `COMPSs` and `permedcoe` modules

   ```bash
   export COMPSS_PYTHON_VERSION=3-ML
   module load COMPSs/2.9
   module load singularity/3.5.2
   module use /apps/modules/modulefiles/tools/COMPSs/libraries
   module load permedcoe
   ```

   > **TIP**: Include the loading into yout `${HOME}/.bashrc` file to load it automatically on the session start.

   This commands will load COMPSs and the permedcoe package which provides all necessary dependencies, as well as the path to the singularity container images (`COVID19_BB_IMAGES` environment variable), assets (`COVID19_BB_ASSETS` environment variable) and testing dataset (`COVID19_PILOT_DATASET` environment variable).

   > **TIP**: It also provides an alias to ease the access to resources: `goto_covid19pilotresources`

2. Get a copy of the pilot workflow into your desired folder

   ```bash
   cd desired_folder
   get_covid19pilotworkflow
   ```

3. Go to `covid19_pilot_workflow/PyCOMPSs` folder
4. Execute `./launch.sh`

This command will launch a job into the job queuing system (Slurm) requesting 2 nodes (one node acting half master and half worker, and other full worker node) for 20 minutes, and is prepared to use the singularity images that are already deployed in MN4 (located into the `COVID19_BB_IMAGES` environment variable). It uses the assets located into the `COVID19_BB_ASSETS` environment variable and dataset located into `COVID19_PILOT_DATASET` environment variable.

> :warning: **TIP**: If you want to run the workflow with a different dataset, please override the `COVID19_PILOT_DATASET` environment variable (or update the `dataset` variable into the `launch.sh` script) with your desired dataset path.

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
