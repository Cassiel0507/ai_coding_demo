import pytest

from param6_check import merge_results


def test_new_override_old():
    old = {("R1", "T1"): 0.8, ("R2", "T2"): 0.7}
    new = {("R1", "T1"): 0.9, ("R3", "T3"): 0.6}
    res = merge_results(old, new)
    assert res[("R1", "T1")] == 0.9
    assert res[("R2", "T2")] == 0.7
    assert res[("R3", "T3")] == 0.6
    assert len(res) == 3

def test_old_empty():
    old = {}
    new = {("R1", "T1"): 0.5}
    res = merge_results(old, new)
    assert res == {("R1", "T1"):0.5}

def test_new_empty():
    old = {("R1", "T1"): 0.5}
    new = {}
    res = merge_results(old, new)
    assert res == {("R1", "T1"):0.5}

def test_both_empty():
    res = merge_results({}, {})
    assert res == {}

def test_input_not_dict():
    with pytest.raises(TypeError):
        merge_results([1,2], {("R1","T1"):0.1})
    with pytest.raises(TypeError):
        merge_results({("R1","T1"):0.1}, 123)

def test_invalid_key():
    # key不是二元tuple
    bad_old = {"R1-T1": 0.2}
    good_new = {("R1", "T1"):0.3}
    with pytest.raises(ValueError):
        merge_results(bad_old, good_new)
    # tuple里面不是字符串
    bad_old2 = {(111, "T1"):0.2}
    with pytest.raises(ValueError):
        merge_results(bad_old2, good_new)

def test_original_not_mutated():
    old = {("R1", "T1"):0.1}
    new = {("R1", "T1"):0.2}
    merge_results(old, new)
    assert old[("R1","T1")] == 0.1
    assert new[("R1","T1")] == 0.2
