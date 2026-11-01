import numpy as np

from param7_check import check_data


def test_all_same_length():
    # 全部长度相同，预期True
    assert check_data([1,2], [3,4], [5,6], [7,8]) == True

def test_x_different():
    # X长度不一样
    assert check_data([1], [3,4], [5,6], [7,8]) == False

def test_y_different():
    # Y长度不一样
    assert check_data([1,2], [3], [5,6], [7,8]) == False

def test_recipes_different():
    # recipes长度不一样
    assert check_data([1,2], [3,4], [5], [7,8]) == False

def test_tools_different():
    # tools长度不一样
    assert check_data([1,2], [3,4], [5,6], [7]) == False

def test_numpy_array_same():
    # numpy数组，长度一致
    X = np.array([1,2,3])
    Y = np.array([4,5,6])
    recipes = np.array([7,8,9])
    tools = np.array([10,11,12])
    assert check_data(X, Y, recipes, tools) == True

def test_numpy_array_diff():
    # numpy数组，长度不一致
    X = np.array([1,2])
    Y = np.array([4,5])
    recipes = np.array([7,8])
    tools = np.array([10])
    assert check_data(X, Y, recipes, tools) == False
