import numpy as np
import pytest

from param5_check import validate_candidate


def test_multi_hit_samples():
    X = np.array([
        [1.0, 2.0],
        [1.1, 2.1],
        [3.0, 2.0],
        [1.0, 5.0]
    ])
    Y = np.array([10, 20, 30, 40])
    candidate = np.array([1.0, 2.0])
    radius = 0.2
    count, mean_y = validate_candidate(X, Y, candidate, radius)
    assert count == 2
    assert mean_y == 15.0

def test_no_hit():
    X = np.array([[5,6],[7,8]])
    Y = np.array([1,2])
    candidate = np.array([1,2])
    radius = 0.1
    count, mean_y = validate_candidate(X, Y, candidate, radius)
    assert count == 0
    assert mean_y is None

def test_radius_zero_exact_match():
    X = np.array([[2,3], [2,3], [4,5]])
    Y = np.array([5, 7, 9])
    candidate = np.array([2,3])
    radius = 0.0
    count, mean_y = validate_candidate(X, Y, candidate, radius)
    assert count == 2
    assert mean_y == 6.0

def test_empty_x():
    X = np.empty((0, 2))
    Y = np.array([])
    candidate = np.array([1,1])
    radius = 0.5
    count, mean_y = validate_candidate(X, Y, candidate, radius)
    assert count == 0
    assert mean_y is None

def test_radius_negative_raise():
    X = np.array([[1,2]])
    Y = np.array([10])
    candidate = np.array([1,2])
    with pytest.raises(ValueError):
        validate_candidate(X, Y, candidate, -0.1)

def test_sample_count_mismatch():
    X = np.array([[1,2],[3,4]])
    Y = np.array([10])
    candidate = np.array([1,2])
    radius = 0.5
    with pytest.raises(ValueError):
        validate_candidate(X, Y, candidate, radius)

def test_feature_dim_mismatch():
    X = np.array([[1,2],[3,4]])
    Y = np.array([10,20])
    candidate = np.array([1])
    radius = 0.5
    with pytest.raises(ValueError):
        validate_candidate(X, Y, candidate, radius)

def test_not_ndarray_type():
    X_list = [[1,2]]
    Y_arr = np.array([10])
    cand = np.array([1,2])
    with pytest.raises(TypeError):
        validate_candidate(X_list, Y_arr, cand, 0.5)
