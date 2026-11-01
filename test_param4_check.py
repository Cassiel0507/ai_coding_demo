import pytest
import pandas as pd
import numpy as np
from param4_check import summarize

def test_normal_group_with_nan():
    data = [
        ["ToolA", "R1", 10.0],
        ["ToolA", "R1", 20.0],
        ["ToolA", "R1", np.nan],
        ["ToolA", "R2", 30.0],
        ["ToolB", "R1", 40.0],
    ]
    df = pd.DataFrame(data, columns=["ToolName", "RECIPE_NAME", "ImplantCurrent"])
    out = summarize(df)
    # ToolA,R1：有效2行，均值15；ToolA,R2：1行均值30；ToolB,R1：1行均值40
    assert out.loc[("ToolA", "R1"), "count"] == 2
    assert out.loc[("ToolA", "R1"), "mean_current"] == 15.0
    assert out.loc[("ToolA", "R2"), "count"] == 1
    assert out.loc[("ToolB", "R1"), "mean_current"] == 40.0

def test_group_all_nan_current():
    data = [
        ["ToolA", "R1", np.nan],
        ["ToolA", "R1", np.nan],
        ["ToolB", "R2", 5.0],
    ]
    df = pd.DataFrame(data, columns=["ToolName", "RECIPE_NAME", "ImplantCurrent"])
    out = summarize(df)
    assert ("ToolA", "R1") not in out.index
    assert out.loc[("ToolB", "R2"), "count"] == 1

def test_empty_input_df():
    df = pd.DataFrame(columns=["ToolName", "RECIPE_NAME", "ImplantCurrent"])
    out = summarize(df)
    assert out.empty
    assert list(out.columns) == ["count", "mean_current"]
    assert isinstance(out.index, pd.MultiIndex)

def test_missing_column_raise_valueerror():
    # 删掉 ImplantCurrent
    df = pd.DataFrame([["T1","R1"]], columns=["ToolName","RECIPE_NAME"])
    with pytest.raises(ValueError):
        summarize(df)

def test_key_column_has_nan_raise_valueerror():
    data = [
        [np.nan, "R1", 10],
        ["ToolA", "R2", 20]
    ]
    df = pd.DataFrame(data, columns=["ToolName", "RECIPE_NAME", "ImplantCurrent"])
    with pytest.raises(ValueError):
        summarize(df)

def test_input_not_dataframe_raise_typeerror():
    with pytest.raises(TypeError):
        summarize([1,2,3])
    with pytest.raises(TypeError):
        summarize({"a":1})
