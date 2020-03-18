import neural_networks.nnm_coordinate as nnm_coordinate

filename = '1gzc'
seed = 23
size = 0.2


def test_medium_model():
    assert nnm_coordinate.medium_model().dtype == 'float32',\
           'The data type is wrong.'


def test_load_csv(filename):
    assert len(nnm_coordinate.load_csv(filename)) == 2,\
           'The length of load_csv output is wrong.'


def test_validation_split(filename, size, seed):
    assert len(nnm_coordinate.validation_split(filename, size, seed)) == 4,\
           'The length of validation_split output is wrong.'


def test_run_model(filename):
    assert len(nnm_coordinate.run_model(filename)) == 2,\
           'The length of run_model output is wrong.'


def test_validation_coord(filename):
    assert len(nnm_coordinate.validation_coord(filename)) == 2,\
           'The length of run_model output is wrong.'


def test_get_mse(filename):
    assert isinstance(nnm_coordinate.get_mse('1gzc'), type(None)),\
           'The type of get_mse output is wrong.'
