'''
This module tests the overall module pdb_autofill inputs.
'''


import pdb_autofill as pdb


def test_pdb_autofill():
    '''
    This funciton tests the pdb_autofill function inputs. 
    '''
    directory = 'small_sample/'
    protein_list = ['1gey', '1gzc', '1ufo', '2hi2', '2jfk', '2o73', '2qqt', '2x82',
                '2y39', '2z91', '3d5m', '3gem', '3qun', '3ueo', '4bal', '4msw',
                '4wji', '4y79', '5uez', '7fdr']
    row = 5
    pdb.pdb_autofill(directory, protein_list, row)

    assert np.dtype(row) == 'int', 'input row datatype is wrong'
    assert np.dtype(directory) == 'str', 'input directory datype is wrong'

    return
