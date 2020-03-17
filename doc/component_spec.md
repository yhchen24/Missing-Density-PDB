# Component Specification

## Sequence Diagram

The sequence diagram for PDB Autofill is included here to show the necessary components for classifying and predicting missing densities in PDB files in this package.

![sequence_diagram](sequence_diagram.png "sequence_diagram")


## Component Cards

Each component card describes what the component does, what are the inputs, what are the outputs, and how it interacts with other components in the package.


**User interface**
  * What it does: Collects information from the user.
  * Inputs: PDB dataset that includes proteins with missing densities and proteins without missing densities. Experimental information and protein sequence is optional if interested in determining whether an experiment is likely to result in missing densities.
  * Outputs: PDB datasets and/or experimental conditions from user.
  * How it interacts with other components: It sends PDB files to the data processing component and experimental conditions to the decision tree component.


**Data processing**
  * What it does: Extracts amino acid sequences, experimental resolution, maximum anisotropic B factor, number of anisotropic B factors over 50, sequence lengths, number of electrically charged residues, number of hydrophobic residues, number of special case residues, number of nonpolar residues, and coordinates of atoms.
  * Inputs: PDB datasets from the user.
  * Outputs: Extracted features from PDB files.
  * How it interacts with other components: Sends extracted features to the decision tree and random forest components. Sends extracted coordinates and features to the neural network model component.


**Decision tree**
  * What it does: Determines whether or not certain experimental conditions for X-ray crystallography will result in missing densities.  
  * Inputs: Experimental conditions and protein sequence from the user. Extracted features from PDB files.
  * Outputs: True/False to the user (will result in missing densities).
  * How it interacts with other components: Receives input of experimental data from the user interface component. Receives input from data processing component. Sends output to the user interface component.


**Random forest**
  * What it does: Classifies the reason behind missing densities in PDB files according to features extracted during data processing.
  * Inputs: Extracted features of interest from PDB files.
  * Outputs: Reason behind missing densities in PDB files.
  * How it interacts with other components: Receives input from data processing component, and sends output to the user interface component.


**Neural network**
  * What it does: Predicts missing coordinates based on PDB training datasets and features/coordinates extracted from data processing.
  * Inputs: Extracted coordinates and features of interest from PDB files.
  * Outputs: Prediction of missing coordinates.
  * How it interacts with other components: Inputs are received from the data processing component, and outputs are sent to the user interface. 


## User Interface

Any python environment can be used as the user interface with this package. For our examples we use [Jupyter Notebook](https://jupyter.org/install).


## Milestones

1. Extract a dataset from PDB consisting of 500 proteins with missing densities and 500 without missing densities
2. Extract useful information about each protein in our dataset to feed into the random forest model
3. Milestone 1: classify the reason behind missing densities using a random forest model
4. Milestone 2 (stretch goal): predict the missing 3D coordinates using a neural network
