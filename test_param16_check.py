import numpy as np

from param16_check import clean_and_get_p1_p99


def test_normal_data_remove_nan_row():
    arr = np.array([[1, 10], [2, np.nan], [3, 30], [4, 40]])
    feats = ["f0", "f1"]
    res = clean_and_get_p1_p99(arr, feats)
    assert res is not None
    assert "f0" in res
    assert "f1" in res

def test_row_with_inf_single_left():
    arr = np.array([[5, 6], [np.inf, 7]])
    feats = ["f0", "f1"]
    res = clean_and_get_p1_p99(arr, feats)
    assert res["f0"][0] == 5
    assert res["f0"][1] == 5
    assert res["f1"][0] == 6
    assert res["f1"][1] == 6

def test_all_rows_invalid_return_none():
    arr = np.array([[np.nan, 1], [2, -np.inf]])
    feats = ["f0", "f1"]
    res = clean_and_get_p1_p99(arr, feats)
    assert res is None

def test_feat_name_length_mismatch():
    arr = np.array([[1,2],[3,4]])
    feats = ["f0"]
    res = clean_and_get_p1_p99(arr, feats)
    assert res is None

def test_input_1d_array():
    arr = np.array([1,2,3])
    feats = ["f0"]
    res = clean_and_get_p1_p99(arr, feats)
    assert res is None
