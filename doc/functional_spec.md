# Functional Specification


## Purpose

The **goal of PDB Autofill is to classify the reason for missing densities** in crystallographic data from the Protein Data Bank (PDB). Additionally, the user can access the protein sequence and extracted features in a Pandas DataFrame.

If time permits, the stretch goal is to then predict the x-y-z positions of missing densities found in PDB files.


## Example Use Cases

Alice is a computational scientist who will be using the tool to determine the expected structure of her proteins of interest. She is very comfortable using python packages to analyze her data.

* Alice will use this package to classify why her proteins of interest have missing densities in the PDB.
* Alice will use this package to predict the missing densities in her proteins of interest.
* Alice may also be interested in using the package to extract amino acid sequences and features in a DataFrame to perform further analysis on her own.


Joe is new to data science and is interested in learning more about PDB files. He has experience using Excel and other instrumentation softwares.

* Joe will use this package to download a sample dataset of PDB files.
* Joe will use this package to extract interesting features from the PDB files.
* Joe will use this package to classify and predict the missing densities that are not captured in the files.
