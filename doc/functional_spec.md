# Functional Specification


## Purpose

The **goal of PDB Autofill is to classify the reason for missing densities** in crystallographic data from the Protein Data Bank (PDB). Additionally, a user can input experimental resolution and protein of interest sequence to determine whether it will result in missing densities in their X-ray crystallography experiment.

If time permits, the stretch goal is to then predict the x-y-z positions of missing densities found in PDB files.


## Example Use Cases

Josie is a computational scientist who will be using the tool to determine the expected structure of her proteins of interest. She is very comfortable using python packages to analyze her data.

* Josie will use this package to classify the reason her proteins of interest have missing densities in the PDB.
* Josie will use this package to predict the missing densities in her proteins of interest.
* Josie may also be interested in using the package to extract amino acid sequences in a CSV format to perform further analysis on her own.


Joe is an experimentalist who will be using the tool to determine whether he expects to find missing densities in the protein for which he will be collecting X-Ray crystallographic data. He has limited programming experience, but has much experience using Excel and other scientific tools.

* Joe will use this package to determine whether he should expect missing densities in his experiment.
* Joes will use this package to classify why some experiments will result in missing densities.
* Joes will use this package to predict the missing densities that are not visible in the experiment.


John is interested in learning why a group of proteins he is studying all have missing densities. He is interested to know whether there is a common feature for why this group of proteins resulted in missing residues.

* John will use this package to classify why the group of proteins he is studying has missing densities.
* John will also use this package to predict the missing densities in his group of proteins and see whether the predictions are similar in structure.
