import pytest
from param19_check import recommend_params

def test_clamp_upper_lower():
    params = {"voltage":120, "speed":50, "gain":2.0}
    bounds = {"voltage":(80,100), "speed":(30,70), "gain":(0,1.5)}
    res = recommend_params(params, bounds)
    assert res == {"voltage":100, "speed":50, "gain":1.5}

def test_extra_param_keep_untouched():
    params = {"a":5, "b":10, "c":99}
    bounds = {"a":(0,10)}
    res = recommend_params(params, bounds)
    assert res == {"a":5, "b":10, "c":99}

def test_bounds_lower_greater_than_upper():
    params = {"x":5}
    bounds = {"x":(20,10)}
    res = recommend_params(params, bounds)
    assert res is None

def test_value_equal_bound():
    params = {"p":10, "q":20}
    bounds = {"p":(10, 30), "q":(5,20)}
    res = recommend_params(params, bounds)
    assert res == {"p":10, "q":20}

def test_clamp_below_lower():
    params={"temp":-10}
    bounds={"temp":(0,100)}
    res = recommend_params(params, bounds)
    assert res == {"temp":0}

def test_bounds_not_two_tuple():
    params={"k":1}
    bounds={"k":(1,2,3)}
    res = recommend_params(params, bounds)
    assert res is None
