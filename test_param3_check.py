import pytest
import numpy as np
from param3_check import get_bounds

def test_normal_with_nan_inf():
    arr = np.array([1,2,3,4,5, np.nan, np.inf, -np.inf, 6,7,8,9,10])
    res = get_bounds(arr)
    assert res is not None
    p1, p99 = res
    assert isinstance(p1, float)
    assert isinstance(p99, float)
    assert p1 <= p99

def test_all_nan_inf():
    arr = np.array([np.nan, np.inf, -np.inf])
    assert get_bounds(arr) is None

def test_only_one_valid_value():
    arr = np.array([5.5, np.nan, np.inf])
    p1, p99 = get_bounds(arr)
    assert p1 == 5.5
    assert p99 == 5.5

def test_empty_1d_array():
    arr = np.array([])
    assert get_bounds(arr) is None

def test_2d_array_raise_valueerror():
    arr = np.array([[1,2],[3,4]])
    with pytest.raises(ValueError):
        get_bounds(arr)

def test_not_numpy_array_raise_typeerror():
    with pytest.raises(TypeError):
        get_bounds([1,2,3])
    with pytest.raises(TypeError):
        get_bounds(123)
    with pytest.raises(TypeError):
        get_bounds(None)
