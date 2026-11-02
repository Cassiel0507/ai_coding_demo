import numpy as np
import pandas as pd

from param15_check import recipe_tool_group_stats


def test_normal_two_groups():
    data = [
        {"Recipe":"R1","Tool":"T1","measurement":10},
        {"Recipe":"R1","Tool":"T1","measurement":20},
        {"Recipe":"R1","Tool":"T2","measurement":30},
        {"Recipe":"R1","Tool":"T2","measurement":40},
    ]
    df = pd.DataFrame(data)
    res = recipe_tool_group_stats(df)
    assert res is not None
    assert res.loc[("R1","T1"), "count"] == 2
    assert res.loc[("R1","T1"), "mean"] == 15
    assert res.loc[("R1","T2"), "count"] == 2
    assert res.loc[("R1","T2"), "mean"] == 35

def test_single_sample_std_nan():
    data = [{"Recipe":"R1","Tool":"T1","measurement":5}]
    df = pd.DataFrame(data)
    res = recipe_tool_group_stats(df)
    assert res.loc[("R1","T1"), "count"] == 1
    assert res.loc[("R1","T1"), "mean"] == 5
    assert np.isnan(res.loc[("R1","T1"), "std"])
    assert res.loc[("R1","T1"), "p95"] == 5

def test_missing_measurement_col():
    df = pd.DataFrame([{"Recipe":"R1","Tool":"T1"}])
    res = recipe_tool_group_stats(df)
    assert res is None

def test_empty_dataframe():
    df = pd.DataFrame(columns=["Recipe","Tool","measurement"])
    res = recipe_tool_group_stats(df)
    assert res is None

def test_contains_nan_in_measurement():
    data = [
        {"Recipe":"R1","Tool":"T1","measurement":10},
        {"Recipe":"R1","Tool":"T1","measurement":np.nan},
        {"Recipe":"R1","Tool":"T1","measurement":30},
    ]
    df = pd.DataFrame(data)
    res = recipe_tool_group_stats(df)
    assert res.loc[("R1","T1"), "count"] == 2
    assert res.loc[("R1","T1"), "mean"] == 20
