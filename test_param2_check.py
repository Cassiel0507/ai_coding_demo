import pytest
from param2_check import get_top_features

def test_more_than_three_valid():
    # 满足条件 >0.1 的有4个，取top3降序
    imp = {"f1": 0.8, "f2": 0.5, "f3": 0.3, "f4": 0.15, "f5": 0.05}
    assert get_top_features(imp) == ["f1", "f2", "f3"]

def test_exactly_three_valid():
    imp = {"a": 0.22, "b": 0.18, "c": 0.12}
    assert get_top_features(imp) == ["a", "b", "c"]

def test_less_than_three_valid():
    imp = {"x": 0.3, "y": 0.05}
    assert get_top_features(imp) == ["x"]

def test_all_below_threshold():
    imp = {"p1": 0.01, "p2": 0.1, "p3": -0.2}
    assert get_top_features(imp) == []

def test_empty_dict():
    imp = {}
    assert get_top_features(imp) == []

def test_negative_score_filtered():
    imp = {"featA": -0.5, "featB": 0.15}
    assert get_top_features(imp) == ["featB"]

def test_input_not_dict():
    with pytest.raises(TypeError):
        get_top_features([1,2,3])
    with pytest.raises(TypeError):
        get_top_features(None)

def test_dict_value_not_numeric():
    imp = {"f1": "high", "f2": 0.2}
    with pytest.raises(TypeError):
        get_top_features(imp)
