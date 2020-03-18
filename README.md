![Logo](doc/Logo.png "Logo")

PDB autofill classifies the reason behind missing electron densities in crystallographic experimental data from the Protein Data Bank, predicts the structure of the missing densities, and predicts whether a new X-ray crystallography experiment will result in missing residues.

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)
<a href="https://github.com/badges/shields/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/badges/shields" /></a>

## Table of Contents

<!--ts-->
  * [Features](#features)
  * [Example](#example)
  * [Installation](#installation)
  * [Team](#team)
  * [Support](#support)
  * [License](#license)
<!--te-->


## Features

* Classify the reason for missing residues in PDB files according to features as described below
* Data processing of PDB files. Features available to extract in this module include: protein sequences to DataFrame, resolution of experiment, maximum anisotropic B factor in protein, and number of hydrophobic/nonpolar/electrically charged/special case residues
* Prediction of missing residue coordinates.
* A sample dataset is available for use in this package for users that are new to PDB files


## Example
```
import getdata
import PDB_Data_Processing

# downloads sample dataset into your local machine
getdata.get_samples()

# names of PDB files to explore
protein_list = ['1a0j', '1a3b', '1a7v', '1a09', '1a46', '1a52', '1a55', '1a95', '1ad4', '1adw']

# extract features of interest to dataframe
pdb.extracted_features('small_sample/', protein_list)

```


## Installation
1. Install Biopython on your local machine

    `conda install biopython`

    Please see [https://biopython.org](https://biopython.org) or [https://github.com/biopython/biopython](https://github.com/biopython/biopython) for further details.

2. Install Keras on your local machine

    `conda install tensorflow`

    `conda install keras`

    Please see [https://keras.io/](https://keras.io/) or [https://github.com/keras-team/keras](https://github.com/keras-team/keras) for further details.

3. Clone the git repository in the folder in which the package will be used. Choose one of the clone methods below.

    Option 1: Clone the repository on your local machine using terminal

    `git clone https://github.com/yhchen24/Missing-Density-PDB.git`

    Option 2: Download the file directly from GitHub and unzip the components (see screenshot below)
![install_instructions](doc/install_instructions.PNG "install_instructions")


## Team
This is Henry, You-Hsin, and Jenny's package!

## Support
Reach out at one of the following places!
* For bug reports or suggestions, please leave issues on [Github](https://github.com/yhchen24/Missing-Density-PDB)
* Twitter at [@jennybennett02](https://twitter.com/jennybennett02)

## License
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
* MIT License
