"""
题目16：清洗异常行 + 计算特征P1/P99边界
需求描述：
输入二维numpy数组（每行一条样本，每列一个特征）、特征名称列表；
第一步：删除任意位置包含 np.nan 或者 np.inf / -np.inf 的整行；
第二步：对清洗之后的每一列（每个特征），分别计算 1% 分位数(P1)、99%分位数(P99)；
返回字典：key为特征名，value为元组 (p1, p99)。
百分位数计算使用 np.percentile，插值方式默认 linear。

输入：
    arr: np.ndarray，二维数组 shape=(样本数, 特征数)
    feature_names: list[str]，特征名称列表，长度必须等于数组列数

输出规则：
    {feat_name: (p1: float, p99: float), ...}

边界 & 异常约定：
    1. arr 不是二维数组 → 返回 None
    2. len(feature_names) != arr.shape[1] → 返回 None
    3. 清洗之后没有剩余样本（全部行都带nan/inf）→ 返回 None
    4. 原始数组本身是空（0行）→ 返回 None
    5. 只剔除【该行任意一列存在nan/inf】的行；正常数值保留
    6. 分位数基于清洗后的干净数据列计算
    7. 不校验feature_names元素重复，交由调用方保证
    8. 允许数值为负数，分位数正常计算

验收用例清单（本需求配套）
用例1：正常混合数据，一行含nan被删掉
arr = np.array([[1, 10], [2, np.nan], [3, 30], [4,40]])
feat_names = ["f0","f1"]
清洗后剩下行：[1,10], [3,30], [4,40]
f0: [1,3,4]  P1≈1.04, P99≈3.96
f1: [10,30,40] P1≈10.4, P99≈39.6

用例2：一行带+inf直接剔除
arr = np.array([[5,6],[np.inf,7]])
feat_names=["f0","f1"]
清洗只剩 [5,6]，单列只有一个样本，P1、P99都等于该值

用例3：全部行都有nan/inf → 返回 None
arr = np.array([[np.nan, 1], [2, -np.inf]])
feat_names=["f0","f1"]

用例4：特征名称数量和列数不匹配 → 返回 None
arr = np.array([[1,2],[3,4]])
feat_names=["f0"]

用例5：输入一维数组，不是二维 → 返回 None
arr = np.array([1,2,3])
feat_names=["f0"]
"""
import numpy as np


def clean_and_get_p1_p99(arr: np.ndarray, feature_names: list[str]):
    if not isinstance(arr, np.ndarray) or arr.ndim != 2 or arr.shape[0] == 0:
        return None
    if len(feature_names) != arr.shape[1]:
        return None

    # 删除包含非有限值的行，再逐列计算 P1 和 P99
    clean_arr = arr[np.isfinite(arr).all(axis=1)]
    if clean_arr.shape[0] == 0:
        return None

    return {
        name: tuple(np.percentile(clean_arr[:, i], [1, 99]))
        for i, name in enumerate(feature_names)
    }
