import numpy as np

from param12_check import extract_harmonic_amplitude


def test_normal_harmonic_inside_range():
    f1 = 10
    freq = np.array([5, 10, 20, 30, 40, 50])
    amp = np.array([0.1, 1.0, 0.8, 0.6, 0.4, 0.2])
    assert extract_harmonic_amplitude(f1, freq, amp) == [0.8, 0.6, 0.4]

def test_harmonic_beyond_right_edge():
    f1 = 20
    freq = np.array([10, 20, 30])
    amp = np.array([1, 2, 3])
    assert extract_harmonic_amplitude(f1, freq, amp) == [3, 3, 3]

def test_harmonic_below_left_edge():
    f1 = 1
    freq = np.array([10, 20, 30])
    amp = np.array([5, 6, 7])
    assert extract_harmonic_amplitude(f1, freq, amp) == [5, 5, 5]

def test_equal_distance_pick_earlier_index():
    f1 = 10
    freq = np.array([18, 22, 30, 34, 40, 44])
    amp = np.array([10, 20, 30, 40, 50, 60])
    assert extract_harmonic_amplitude(f1, freq, amp) == [10, 30, 50]

def test_freq_amp_length_mismatch():
    f1 = 10
    freq = np.array([10,20])
    amp = np.array([1])
    assert extract_harmonic_amplitude(f1, freq, amp) is None

def test_f1_zero_or_negative():
    freq = np.array([10,20,30])
    amp = np.array([1,2,3])
    assert extract_harmonic_amplitude(0, freq, amp) is None
    assert extract_harmonic_amplitude(-5, freq, amp) is None

def test_empty_freq_array():
    f1 = 10
    freq = np.array([])
    amp = np.array([1,2,3])
    assert extract_harmonic_amplitude(f1, freq, amp) is None
