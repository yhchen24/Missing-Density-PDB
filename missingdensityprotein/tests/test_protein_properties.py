import pandas as pd
import protein_properties

'''
This module includes test functions for functions within the
protein_properties module.
'''

def test_electrically_charged_residues():
    '''
    This function tests the electrically_charged_residues function in
    pdbautofill.
    '''
    protein_sequence = pd.read_csv('small_sample_res.csv')
    result = protein_properties.electrically_charged_residues(protein_sequence)

    assert len(result) == len(protein_sequence.columns), 'Output is the wrong \
        length.'
    assert np.shape(result) == (len(protein_sequence.columns), 1), 'Output is \
        the wrong size.'
    assert dtype(protein_sequence[0]) == 'str', 'Input datatype is not "str"'
    assert result[0] == 61, 'Incorrect result values'


def test_unpolar_residues():
    '''
    This function tests the unpolar_residues function in pdbautofill
    '''
    protein_sequence = pd.read_csv('small_sample_res.csv')
    result = protein_properties.unpolar_residues(protein_sequence)

    assert len(result) == len(protein_sequence.columns), 'Output is the wrong \
        length.'
    assert np.shape(result) == (len(protein_sequence.columns), 1), 'Output is \
        the wrong size.'
    assert dtype(protein_sequence[0]) == 'str', 'Input datatype is not "str"'
    assert result[0] == 50, 'Incorrect result values.'


def test_hydrophobic_residues():
    '''
    This function tests the hydrophobic_residues function in pdbautofill
    '''
    protein_sequence = pd.read_csv('small_sample_res.csv')
    result = protein_properties.hydrophobic_residues(protein_sequence)

    assert len(result) == len(protein_sequence.columns), 'Output is the wrong \
        length.'
    assert np.shape(result) == (len(protein_sequence.columns), 1), 'Output is \
        the wrong size.'
    assert dtype(protein_sequence[0]) == 'str', 'Input datatype is not "str"'
    assert result[0] == 75, 'Incorrect result values.'


def test_special_residues():
    '''
    This function tests the special_residues function in pdbautofill
    '''
    protein_sequence = pd.read_csv('small_sample_res.csv')
    result = protein_properties.special_residues(protein_sequence)

    assert len(result) == len(protein_sequence.columns), 'Output is the wrong \
        length.'
    assert np.shape(result) == (len(protein_sequence.columns), 1), 'Output is \
        the wrong size.'
    assert dtype(protein_sequence[0]) == 'str', 'Input datatype is not "str"'
    assert result[0] == 18, 'Incorrect result values.'


def test_residue_groups():
    '''
    This function tests the residue_groups function in pdbautofill
    '''
    protein_sequence = pd.read_csv('small_sample_res.csv')
    result = protein_properties.residue_groups(protein_sequence)

    assert len(result) == len(protein_sequence.columns), 'Output is the wrong \
        length.'
    assert np.shape(result) == (len(protein_sequence.columns), 5), 'Output is \
        the wrong size.'
    assert dtype(protein_sequence[0]) == 'str', 'Input datatype is not "str"'
