import numpy as np
import pytest

from param10_check import freq_range_rms


def test_normal_case_mixed_freq():
    # 常规：包含区间内、低于、高于的点，包含边界0.02和0.1
    freq = np.array([0.01, 0.02, 0.05, 0.1, 0.15])
    amp = np.array([2, 4, 6, 8, 10])
    selected, rms = freq_range_rms(freq, amp)
    np.testing.assert_array_equal(selected, np.array([4,6,8]))
    expected_rms = np.sqrt(np.mean(np.array([4,6,8])**2))
    assert np.isclose(rms, expected_rms)

def test_no_data_in_range():
    # 区间内无数据，rms返回nan
    freq = np.array([0.001, 0.01, 0.11])
    amp = np.array([1,2,3])
    selected, rms = freq_range_rms(freq, amp)
    assert len(selected) == 0
    assert np.isnan(rms)

def test_only_lower_bound():
    freq = np.array([0.02])
    amp = np.array([10])
    selected, rms = freq_range_rms(freq, amp)
    np.testing.assert_array_equal(selected, np.array([10]))
    assert np.isclose(rms, 10.0)

def test_only_upper_bound():
    freq = np.array([0.1])
    amp = np.array([5])
    selected, rms = freq_range_rms(freq, amp)
    assert np.isclose(rms, 5.0)

def test_mismatch_length_raise():
    # 长度不一致，抛ValueError
    freq = np.array([0.02,0.05])
    amp = np.array([1])
    with pytest.raises(ValueError):
        freq_range_rms(freq, amp)

def test_not_numpy_array_raise():
    # 传入list而不是np数组，触发TypeError
    freq = [0.02, 0.05]
    amp = [3,4]
    with pytest.raises(TypeError):
        freq_range_rms(freq, amp)

def test_all_inside_range():
    freq = np.array([0.03, 0.06, 0.09])
    amp = np.array([1,1,1])
    selected, rms = freq_range_rms(freq, amp)
    assert len(selected) == 3
    assert np.isclose(rms, 1.0)
