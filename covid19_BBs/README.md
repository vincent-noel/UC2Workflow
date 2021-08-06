# HPC/Exascale Centre of Excellence in Personalised Medicine

## Gromacs Building Blocks

This package provides a set of **Building Blocks (BB)** for Covid-19 Pilot
using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Covid-19 Pilot Building Blocks](#Covid-19-Pilot-building-blocks)
  - [Table of Contents](#table-of-contents)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [License](#license)
  - [Contact](#contact)

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)

In addtion to the dependencies, it is necessary to download the singularity
images and the building block assets.
They must be available and exported in the following environment variables:

```bash
export COVID19_BB_IMAGES="/path/to/images/"
export COVID19_BB_ASSETS="/path/to/assets/"
```

### Installation

There are two ways to install this package (from Pypi and manually):

- From Pypi:

  This package is **NOT YET** publicly available in Pypi:

  ```bash
  pip install covid19_BBs
  ```

  or more specifically:

  ```bash
  python3 -m pip install covid19_BBs
  ```

- From source code:

  This package provides an automatic installation script:

  ```bash
  ./install.sh
  ```

  This script creates a file `installation_files.txt` to keep track of the
  installed files.
  It is used with the `uninstall.sh` script to clean up the system.

### Usage

The `covid19_BBs` package provides a clear interface that allows it to be
used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and Snakemake).

In particular, provides 4 building blocks:

- MaBoSS
- Single cell analysis
- Personalize model
- PhysiBoSS

These building blocks can be imported from python and invoked directly from
a **PyCOMPSs** application, or through the binaries from other workflow
managers (e.g. Snakemake and NextFlow).

The binaries are:

- MaBoSS

  ```bash
  maboss -d \
      -i <prefix> <data_folder> \
      -o <ko_file> \
      --mount_point ${COVID19_BB_ASSETS}/MaBoSS:${COVID19_BB_ASSETS}/MaBoSS
  ```

- Single cell analysis

  ```bash
  single_cell_processing -d \
      -i <metadata_file(tsv)> \
      -o <result_folder> \
      --mount_points ${COVID19_BB_ASSETS}/single_cell/:${COVID19_BB_ASSETS}/single_cell/
  ```

- Personalize model

  ```bash
  personalize_patient -d \
        -i <normalized_data_file(tsv)> <cells_metadata(tsv)> <data_folder> <model_prefix> <prefix> <ko_file> \
        -o <result_folder> \
        --mount_points ${COVID19_BB_ASSETS}/personalize_patient/:${COVID19_BB_ASSETS}/personalize_patient/,<data_folder>:<data_folder>
  ```

- PhysiBoSS

  ```bash
  physiboss -d \
        -i <sample> <repetition> <prefix> <bnd_file> <cfg_file> \
        -o  <out_file> <err_file>\
        --mount_points ${COVID19_BB_ASSETS}/PhysiBoSS/:${COVID19_BB_ASSETS}/PhysiBoSS/
  ```


### Uninstall

Uninstall can be done as usual `pip` packages:

```bash
pip uninstall covid19_BBs
```

or more specifically:

```bash
./uninstall.sh
./clean.sh
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
