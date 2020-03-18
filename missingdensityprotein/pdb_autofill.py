import dataprocess.PDB_Data_Processing as pdb_dp
import randomforest.Random_Forest as RF


'''
This module is a wrapping function to process data and return the
classification for missing residues in one step.
'''


def pdb_autofill(directory, protein_list, row):
    '''
    This function returns the classification for why a dataset has missing
    densities. (Features include B factor above 50, sequence length, number of
    nonpolar residues, number of electrically charged residues, number of
    hydrophobic residues, and number of special case resides)

    Parameters
    ----------
    directory: file directory of where the PDB files are located, 'str'

    protein_list: a list of the protein names in the file directory

    row: the number in the list you are interested to classify, 'int'
    '''
    # extract features from PDB files
    features = pdb_dp.extracted_features(directory, protein_list)
    features['Protein'] = features['protein']

    # save output features as csv for input of random forest
    features.to_csv('RF_input.csv')

    # use the random forest for classification
    RF.get_reason_prediction('RF_input.csv', row)

    return
