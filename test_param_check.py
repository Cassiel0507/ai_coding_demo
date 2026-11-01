from param_check import find_missing_params


def test_has_missing():
    # 验收样例1：缺pressure
    req = {"temp":100, "pressure":0.5, "time":10}
    inp = {"temp":90, "time":12}
    assert find_missing_params(req, inp) == ["pressure"]

def test_all_ok():
    # 样例2：参数齐全，返回空
    req = {"temp":100}
    inp = {"temp": 80}
    assert find_missing_params(req, inp) == []

def test_all_missing():
    # 样例3：全部缺失
    req = {"a":1, "b":2}
    inp = {}
    assert find_missing_params(req, inp) == ["a","b"]

def test_not_dict_input():
    # 异常测试：输入不是字典
    req = {"a":1}
    inp = 123
    assert find_missing_params(req, inp) == []
