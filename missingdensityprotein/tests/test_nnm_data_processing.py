import dataprocess.nnm_data_processing as nnm_data_processing
import warnings

warnings.filterwarnings("ignore")
complete_file_path = 'ExampleData/Sample/'
missing_file_path = 'ExampleData/Sample/Missing/'
output = 'prac/'


def test_data_processing():
    assert len(nnm_data_processing.data_processing(complete_file_path)) == 2,\
            'The length of data_processing output is wrong.'
    return


def test_save_to_csv():
    assert isinstance(nnm_data_processing.save_to_csv(complete_file_path,
                                                      output), type(None)),\
            'The type of save_to_csv output is wrong.'
    return


def test_num_atoms_of_seq():
    assert len(nnm_data_processing.num_atoms_of_seq()) == 20,\
            'The length of num_atoms_of_seq output is wrong.'
    return


def test_num_miss_atoms():
    assert len(nnm_data_processing.num_miss_atoms(missing_file_path)) ==\
            len(nnm_data_processing.data_processing(missing_file_path)[1]),\
            'The length of num_miss_atoms output is wrong.'
    return
