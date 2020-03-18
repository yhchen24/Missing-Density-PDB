import Random_Forest as RF
import pandas as pd


def test_build_own_model():
    df_train = 'C:/Users/Henry Lee/Desktop/Direct/project/Missing-Density-PDB/model/newsummary_1000.csv'
    assert isinstance(RF.build_own_model(df_train), float) is True, \
        "Warning: Incorrect output"
    return


def get_reason_prediction():
    df_train = 'C:/Users/Henry Lee/Desktop/Direct/project/Missing-Density-PDB/model/newsummary_1000.csv'
    assert isinstance(RF.get_reason_prediction(df_train, 10), bool) is True, \
        "Warning: Incorrect output"
    return
