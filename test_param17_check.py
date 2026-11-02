import pytest
from param17_check import get_top3_features

def test_more_than_three():
    names = ["f1","f2","f3","f4"]
    imp = [0.5, 0.2, 0.7, 0.1]
    assert get_top3_features(names, imp) == ["f3","f1","f2"]

def test_only_two_features():
    names = ["a","b"]
    imp = [0.9,0.3]
    assert get_top3_features(names, imp) == ["a","b"]

def test_same_score_keep_original_order():
    names = ["x","y","z"]
    imp = [0.6,0.6,0.2]
    assert get_top3_features(names, imp) == ["x","y","z"]

def test_length_mismatch():
    names = ["f1"]
    imp = [0.1,0.2]
    assert get_top3_features(names, imp) is None

def test_both_empty():
    assert get_top3_features([], []) == []

def test_negative_importance():
    names = ["p","q","r"]
    imp = [-0.1, -0.5, 0.0]
    assert get_top3_features(names, imp) == ["r","p","q"]
