from param11_check import find_freq_peak


def test_normal_case_find_max():
    data = [(10, 2.2), (20, 5.5), (30, 3.1)]
    assert find_freq_peak(data, 10, 30) == (20, 5.5)

def test_no_data_in_range():
    data = [(10, 2.2), (20, 5.5)]
    assert find_freq_peak(data, 30, 50) is None

def test_same_amplitude_return_first():
    data = [(10, 4.0), (20, 4.0)]
    assert find_freq_peak(data, 10, 20) == (10, 4.0)

def test_min_greater_than_max():
    data = [(1, 10), (2, 20)]
    assert find_freq_peak(data, 20, 10) is None

def test_empty_input_data():
    assert find_freq_peak([], 0, 100) is None

def test_point_exactly_on_boundary():
    data = [(5, 1.1), (10, 9.9)]
    assert find_freq_peak(data, 10, 10) == (10, 9.9)

def test_negative_amplitude():
    data = [(1, -5), (2, -1)]
    assert find_freq_peak(data, 1, 2) == (2, -1)
