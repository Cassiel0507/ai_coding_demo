from param9_check import group_machine_data


def test_sample_case():
    # 题目标准样例
    recipes = ['R1', 'R1', 'R2', 'R1']
    tools = ['T1', 'T1', 'T2', 'T2']
    values = [10, 20, 30, 40]
    res = group_machine_data(recipes, tools, values)
    assert res == {('R1','T1'): [10,20], ('R2','T2'): [30], ('R1','T2'): [40]}
    assert type(res) is dict  # 必须是普通dict，不是defaultdict

def test_single_row():
    # 仅一条数据
    recipes = ['R5']
    tools = ['T9']
    values = [99]
    res = group_machine_data(recipes, tools, values)
    assert res == {('R5','T9'): [99]}

def test_all_unique_pair():
    # 全部组合不重复
    recipes = ['R1','R2','R3']
    tools = ['T1','T2','T3']
    values = [1,2,3]
    res = group_machine_data(recipes, tools, values)
    assert res == {('R1','T1'):[1], ('R2','T2'):[2], ('R3','T3'):[3]}

def test_multi_same_pair_long():
    # 同一组合多条，顺序保留
    recipes = ['R2','R2','R2']
    tools = ['T5','T5','T5']
    values = [5,6,7]
    res = group_machine_data(recipes, tools, values)
    assert res[('R2','T5')] == [5,6,7]
