import nnm_coordinate
import pandas as pd

filename = '1gzc'
seed = 23
size = 0.2


def test_medium_model():
    assert nnm_coordinate.medium_model().dtype == 'float32',\
           'The data type is wrong.'
    return


def test_load_csv():
    assert len(nnm_coordinate.load_csv(filename)) == 2,\
           'The length of load_csv output is wrong.'
    return


def test_validation_split():
    assert len(nnm_coordinate.validation_split(filename, size, seed)) == 4,\
           'The length of validation_split output is wrong.'
    return


def test_run_model():
    assert len(nnm_coordinate.run_model(filename)) == 2,\
           'The length of run_model output is wrong.'
    return


def test_validation_coord():
    assert type(nnm_coordinate.validation_coord(filename)) == pd.DataFrame,\
           'The type of validation_coord output is wrong.'
    return


def test_get_mse():
    assert isinstance(nnm_coordinate.get_mse(filename), type(None)),\
           'The type of get_mse output is wrong.'
    return
