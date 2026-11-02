"""
题目19：参数边界截断推荐 recommend_params
需求描述：
编写函数 recommend_params(params, bounds)
params：参数字典，key=参数名，value=当前参数数值
bounds：边界字典，key=参数名，value=(lower, upper) 元组，代表该参数下限、上限
对每一个在 bounds 里存在的参数：
- 如果参数值 < lower → 截断为 lower
- 如果参数值 > upper → 截断为 upper
- 在 [lower, upper] 区间内 → 保持原值
不在 bounds 中的参数：直接原样保留到结果字典
返回截断完成后的建议参数字典。

输入：
    params: dict[str, float | int]
    bounds: dict[str, tuple[float | int, float | int]]

输出规则：
    dict[str, float | int]，和params键集合一致，数值经过边界截断

边界 & 异常约定：
    1. bounds 里面某个参数的下限 > 上限 → 返回 None
    2. params、bounds 任意一个不是字典类型 → 返回 None
    3. bounds 中 value 不是长度为2的元组 → 返回 None
    4. 只对同时存在于 bounds 的参数做截断；params独有、bounds没有的参数直接原样带出
    5. bounds里有，但params里不存在的参数：忽略，不添加进结果
    6. 等于边界值：不截断，保留原值
    7. 允许数值为负数、0

验收用例清单（本需求配套）
用例1：部分参数超上界、超下界、在区间内
params = {"voltage":120, "speed":50, "gain":2.0}
bounds = {"voltage":(80,100), "speed":(30,70), "gain":(0,1.5)}
voltage=120>100 → 100；speed=50正常；gain=2.0>1.5 →1.5
输出 {"voltage":100, "speed":50, "gain":1.5}

用例2：params存在bounds未定义的参数，原样保留
params = {"a":5, "b":10, "c":99}
bounds = {"a":(0,10)}
输出 {"a":5, "b":10, "c":99}

用例3：边界下限大于上限，非法bounds → 返回 None
params = {"x":5}
bounds = {"x":(20, 10)}

用例4：刚好等于上下边界，不修改
params = {"p":10, "q":20}
bounds = {"p":(10, 30), "q":(5,20)}
输出 {"p":10, "q":20}

用例5：参数低于下限
params={"temp":-10}
bounds={"temp":(0,100)}
输出 {"temp":0}

用例6：bounds里面不是二元元组 → 返回 None
params={"k":1}
bounds={"k":(1,2,3)}
"""

def recommend_params(params, bounds):
    if not isinstance(params, dict) or not isinstance(bounds, dict):
        return None

    result = params.copy()
    for name, limits in bounds.items():
        if not isinstance(limits, tuple) or len(limits) != 2:
            return None
        lower, upper = limits
        if lower > upper:
            return None
        if name in result:
            # 将已配置的参数值截断到合法区间
            result[name] = min(max(result[name], lower), upper)
    return result
