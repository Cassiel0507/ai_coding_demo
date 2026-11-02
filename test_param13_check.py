from param13_check import count_abnormal_features


def test_case1_alarm_equal_threshold():
    fft = [2.1, 1.5, 3.0, 1.9]
    env = [1.0, 2.5, 2.0, 0.8]
    assert count_abnormal_features(fft, env, 3) == (2, 1, True)

def test_case2_sum_below_threshold_no_alarm():
    fft = [2.1, 1.1, 1.2, 1.3]
    env = [1.4, 1.5, 1.6, 1.7]
    assert count_abnormal_features(fft, env, 3) == (1, 0, False)

def test_case3_all_equal_two_no_over():
    fft = [2, 2, 2, 2]
    env = [2, 2, 2, 2]
    assert count_abnormal_features(fft, env, 1) == (0, 0, False)

def test_case4_all_over_two():
    fft = [3, 4, 5, 6]
    env = [2.2, 2.3, 2.4, 2.5]
    assert count_abnormal_features(fft, env, 5) == (4, 4, True)

def test_fft_length_not_4():
    fft = [2.1, 3.0]
    env = [1,2,3,4]
    assert count_abnormal_features(fft, env, 2) is None

def test_env_length_not_4():
    fft = [1,2,3,4]
    env = [2.2]
    assert count_abnormal_features(fft, env, 2) is None

def test_threshold_zero_invalid():
    fft = [2.1, 2.2, 1, 1]
    env = [1,1,1,1]
    assert count_abnormal_features(fft, env, 0) is None

def test_negative_values():
    fft = [-1, -2, 2.5, 1.0]
    env = [2.1, -5, 0, 1.8]
    assert count_abnormal_features(fft, env, 2) == (1, 1, True)
