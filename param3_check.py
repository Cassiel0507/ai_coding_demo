"""
需求：题目3 计算工艺参数上下界
函数：get_bounds(values)

【输入】
values: numpy.ndarray 一维数组，存放工艺参数数值
允许数组内包含正常数字、NaN、Inf、-Inf

【处理步骤顺序】
1. 过滤：剔除数组中的 NaN、Inf、-Inf，只保留有限有效数值
2. 判断：过滤后如果没有剩下有效数据，返回 None
3. 计算：对剩下有效数据，计算分位数 P1（1%分位）、P99（99%分位）
4. 输出：返回元组 (p1, p99)，两个都是 float

【异常约定】
- 输入不是 numpy 数组：抛出 TypeError
- 输入是多维 numpy 数组：抛出 ValueError，只支持一维数组

【验收标准（测试点）】
1. 正常一维数组，少量NaN/Inf，过滤后有足够数据，正确返回P1、P99
2. 全部都是 NaN / Inf，过滤后无有效数据 → 返回 None
3. 数组只有1个有效数字：P1、P99都等于这个数字
4. 输入空的一维numpy数组 → 返回 None
5. 输入多维numpy数组（2D）→ 抛 ValueError
6. 输入list、int等非ndarray类型 → 抛 TypeError
"""
import numpy as np


def get_bounds(values):
    # 只接受一维 numpy 数组
    if not isinstance(values, np.ndarray):
        raise TypeError("values must be a numpy.ndarray")
    if values.ndim != 1:
        raise ValueError("values must be a 1D numpy array")

    # 过滤掉 NaN、Inf、-Inf，只保留有限有效值
    valid = values[np.isfinite(values)]
    if valid.size == 0:
        return None

    # 统一使用 0.01 / 0.99 分位数，返回浮点数元组
    p1, p99 = np.quantile(valid, [0.01, 0.99])
    return float(p1), float(p99)
