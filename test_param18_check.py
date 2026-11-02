import pytest
from param18_check import merge_recipe_tool_result

def test_mix_new_update_unchanged():
    old = {("R1","T1"):10, ("R1","T2"):20, ("R2","T1"):30}
    new = {("R1","T1"):99, ("R1","T3"):40}
    merged, cnt_new, cnt_upd, cnt_unch = merge_recipe_tool_result(old, new)
    assert merged[("R1","T1")] == 99
    assert merged[("R1","T2")] == 20
    assert merged[("R2","T1")] == 30
    assert merged[("R1","T3")] == 40
    assert cnt_new == 1
    assert cnt_upd == 1
    assert cnt_unch == 2

def test_new_empty():
    old = {("R1","T1"):5}
    new = {}
    merged, cnt_new, cnt_upd, cnt_unch = merge_recipe_tool_result(old, new)
    assert merged == old
    assert cnt_new == 0
    assert cnt_upd == 0
    assert cnt_unch == 1

def test_old_empty_all_new():
    old = {}
    new = {("R1","T1"):7}
    merged, cnt_new, cnt_upd, cnt_unch = merge_recipe_tool_result(old, new)
    assert merged[("R1","T1")] ==7
    assert cnt_new ==1
    assert cnt_upd ==0
    assert cnt_unch ==0

def test_all_keys_overlap():
    old = {("R1","T1"):1}
    new = {("R1","T1"):2}
    merged, cnt_new, cnt_upd, cnt_unch = merge_recipe_tool_result(old, new)
    assert cnt_new ==0
    assert cnt_upd ==1
    assert cnt_unch ==0

def test_input_not_dict():
    res = merge_recipe_tool_result([1,2,3], {})
    assert res is None
