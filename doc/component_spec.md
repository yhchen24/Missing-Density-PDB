## Component spec (Draft)

![sequence_diagram](doc/sequence_diagram.png "sequence_diagram")

Use the use cases and things mentioned in them to create components

For the previous examples provided:
Two top level components come up right away

1. A database
2. A user interface
3.

(likely many more and some that are sub-components of the above. For each component, you can use the following template to create a component 'card' in the form:



* Name
* What it does
* Inputs (with type information)
* Outputs (with type information
* How it interacts with other components

### User Interface

The user interface for this software is any python environment. (If you are new to python, we recommend [Jupyter Notebook](https://jupyter.org/install)).


### Milestones

1. Extract a dataset from PDB consisting of 500 proteins with missing densities and 500 without missing densities
2. Extract useful information about each protein in our dataset to feed into the random forest model
3. Milestone 1: classify the reason behind missing densities using a random forest model
4. Milestone 2 (stretch goal): predict the missing 3D coordinates using a neural network
