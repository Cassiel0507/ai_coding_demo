from param14_check import rule_check


def test_A_trigger_alarm():
    assert rule_check("ADPOL01_2A", 6, 11) == 1

def test_A_feat2_not_enough():
    assert rule_check("ADPOL01_2A", 6, 9) == 0

def test_B_trigger_alarm():
    assert rule_check("ADPOL01_2B", 8, 13) == 1

def test_B_equal_threshold_no_trigger():
    assert rule_check("ADPOL01_2B", 7, 12) == 0

def test_unknown_device():
    assert rule_check("ADPOL99", 100, 200) == 0

def test_A_feat1_not_enough():
    assert rule_check("ADPOL01_2A", 4, 15) == 0

def test_negative_feature():
    assert rule_check("ADPOL01_2A", -1, -2) == 0
