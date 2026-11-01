"""
题目9：按 Recipe + Tool 分组
【输入】
recipes：list，配方标识
tools：list，工具标识
values：list，待分组的数值
约束：三个列表长度必须相同
【输出】
普通dict（不是defaultdict）；key是元组 (recipe, tool)，value是该组合对应的所有values组成的list
要求内部实现必须使用 collections.defaultdict(list) 做分组，最后转为普通字典返回
【异常约定】
1. 如果三个列表长度不一致，不主动捕获异常，抛出原生异常
2. 允许recipe、tool为字符串；value可以是数字，不做类型校验
【验收标准】
1. 样例输入：
recipes = ['R1', 'R1', 'R2', 'R1']
tools = ['T1', 'T1', 'T2', 'T2']
values = [10, 20, 30, 40]
输出：
{('R1','T1'): [10,20], ('R2','T2'): [30], ('R1','T2'): [40]}
2. 同一个(recipe,tool)多条数据，value顺序保持输入先后顺序
3. 输入只有一组数据，字典只有一个key
4. 无重复组合，每个key只包含一个value
5. 返回类型是dict，不能直接返回defaultdict
"""
from collections import defaultdict


def group_machine_data(recipes, tools, values):
    # 按配方和工具分组，保留输入顺序
    groups = defaultdict(list)
    for recipe, tool, value in zip(recipes, tools, values):
        groups[(recipe, tool)].append(value)
    return dict(groups)
