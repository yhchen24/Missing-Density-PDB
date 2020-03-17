# Component Specification

A sequence diagram of PDB Autofill can be seen below indicating the necessary components.

![sequence_diagram](sequence_diagram.png "sequence_diagram")

Each component is described in further detail below:

User interface
  * What it does: Collects information from the user.
  * Inputs: PDB dataset that includes proteins with missing densities and proteins without missing densities. Experimental information is optional if interested in determining whether an experiment is likely to result in missing densities.
  * Outputs: PDB datasets and/or experimental conditions from user.
  * How it interacts with other components: It sends PDB files to the data processing component and experimental conditions to the decision tree component.

Data processing
  * What it does: Extracts amino acid sequences, experimental resolution, maximum anisotropic B factor, number of anisotropic B factors over 50, sequence lengths, number of electrically charged residues, number of hydrophobic residues, number of special case residues, number of nonpolar residues, and coordinates of atoms.
  * Inputs:
  * Outputs:
  * How it interacts with other components:

Decision tree
  * What it does:
  * Inputs:
  * Outputs:
  * How it interacts with other components:

Random forest
  * What it does:
  * Inputs:
  * Outputs:
  * How it interacts with other components:

Neural network
  * What it does:
  * Inputs:
  * Outputs:
  * How it interacts with other components:


## User Interface

Any python environment can be used as a user interface with this package. For our examples we use [Jupyter Notebook](https://jupyter.org/install).


## Milestones

1. Extract a dataset from PDB consisting of 500 proteins with missing densities and 500 without missing densities
2. Extract useful information about each protein in our dataset to feed into the random forest model
3. Milestone 1: classify the reason behind missing densities using a random forest model
4. Milestone 2 (stretch goal): predict the missing 3D coordinates using a neural network
