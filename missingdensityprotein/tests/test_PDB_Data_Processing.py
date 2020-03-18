import numpy as np
import PDB_Data_Processing


'''
This module tests functions in the PDB_Data_Processing module
'''


def test_samples_statistics():
    '''
    This function tests the sample_statistics() function in
    PDB_Data_Processing.py
    '''
    result = PDB_Data_Processing.samples_statistics('small_sample/')
    assert len(result) <= 10, 'result is wrong size'

    return


def test_extraction_residues_headers():
    '''
    This function tests extraction_residues_headers() function in the
    PDB_Data_Processing.py module.
    '''
    protein_list = ['1a0j', '1a3b', '1a7v', '1a09', '1a46', '1a52',
                    '1a55', '1a95', '1ad4', '1adw']
    [res_data, headers] = PDB_Data_Processing.extraction_residues_headers(
                                                'small_sample/', protein_list)

    assert len(res_data.columns) == 10, 'Residue dataframe wrong number \
        of columns'
    assert np.shape(headers) == (10, 10), 'Headers dataframe wrong size.'

    return


def test_extracted_features():
    '''
    This function tests extracted_features() function in
    PDB_Data_Processing module.
    '''
    protein_list = ['1a0j', '1a3b', '1a7v', '1a09', '1a46', '1a52',
                    '1a55', '1a95', '1ad4', '1adw']
    result = PDB_Data_Processing.extracted_features('small_sample/',
                                                    protein_list)

    assert np.shape(result) == (10, 15), 'Result is the wrong size.'
    assert result.columns[0] == 'protein', 'Result outpid is wrong format.'

    return
