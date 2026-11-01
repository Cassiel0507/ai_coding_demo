import numpy as np

from param8_check import sort_machine_data


def test_normal_sort_case():
    # 题目给的标准样例
    time = np.array([300, 100, 200])
    current = np.array([0.03, 0.01, 0.02])
    tools = np.array(['T3', 'T1', 'T2'])
    t_out, c_out, tool_out = sort_machine_data(time, current, tools)
    np.testing.assert_array_equal(t_out, np.array([100, 200, 300]))
    np.testing.assert_array_equal(c_out, np.array([0.01, 0.02, 0.03]))
    np.testing.assert_array_equal(tool_out, np.array(['T1', 'T2', 'T3']))

def test_already_sorted():
    # 已经升序，不变
    time = np.array([10,20,30])
    current = np.array([0.1,0.2,0.3])
    tools = np.array(['A','B','C'])
    t_out, c_out, tool_out = sort_machine_data(time, current, tools)
    np.testing.assert_array_equal(t_out, time)
    np.testing.assert_array_equal(c_out, current)
    np.testing.assert_array_equal(tool_out, tools)

def test_single_element():
    # 仅一条数据
    time = np.array([50])
    current = np.array([0.05])
    tools = np.array(['T5'])
    t_out, c_out, tool_out = sort_machine_data(time, current, tools)
    np.testing.assert_array_equal(t_out, time)
    np.testing.assert_array_equal(c_out, current)
    np.testing.assert_array_equal(tool_out, tools)

def test_duplicate_time():
    # time有相同值，对应关系不能乱
    time = np.array([200, 100, 100])
    current = np.array([0.05, 0.01, 0.02])
    tools = np.array(['T3','T1','T2'])
    t_out, c_out, tool_out = sort_machine_data(time, current, tools)
    assert t_out[0] == 100
    assert t_out[1] == 100
    assert t_out[2] == 200
