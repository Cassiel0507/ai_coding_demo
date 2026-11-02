"""
题目15：分组统计特征（Recipe + Tool）
需求描述：
输入 pandas DataFrame，按照 Recipe、Tool 两列进行分组；
对目标数值列（measurement），每组计算：样本数量count、平均值mean、标准差std、95百分位数p95。
返回汇总后的DataFrame，索引为 Recipe, Tool，列依次为 count, mean, std, p95。

输入：
    df: pd.DataFrame，必须包含 Recipe、Tool、measurement 三列
    目标统计固定作用在 measurement 这一列

输出规则：
    返回分组聚合后的 DataFrame，列名固定：["count", "mean", "std", "p95"]

边界 & 异常约定：
    1. df 缺少 Recipe / Tool / measurement 任意一列 → 返回 None
    2. measurement 列不是数值类型（字符串、object等无法计算统计量）→ 返回 None
    3. 分组内只有1条样本：标准差 std 返回 np.nan（pandas原生行为）
    4. 百分位数使用 np.percentile，参数 q=95，默认线性插值
    5. 空DataFrame输入 → 返回 None
    6. 不处理 measurement 内 NaN：分组聚合时自动跳过 NaN（dropna）
    7. 分组后如果该组全部measurement都是NaN，统计结果为NaN，正常保留该行，不丢弃分组

验收用例清单（本需求配套）
用例1：两组正常数据，多样本
data = [
    {"Recipe":"R1","Tool":"T1","measurement":10},
    {"Recipe":"R1","Tool":"T1","measurement":20},
    {"Recipe":"R1","Tool":"T2","measurement":30},
    {"Recipe":"R1","Tool":"T2","measurement":40},
]
分组(R1,T1): count=2, mean=15, std≈7.071, p95≈19.5
分组(R1,T2): count=2, mean=35, std≈7.071, p95≈39.5

用例2：分组内只有1个样本，std为nan
data = [{"Recipe":"R1","Tool":"T1","measurement":5}]
结果 count=1, mean=5, std=nan, p95=5

用例3：缺失必要列（缺少measurement）→ 返回 None
用例4：输入空DataFrame → 返回 None
用例5：measurement存在NaN，自动跳过NaN
data = [
    {"Recipe":"R1","Tool":"T1","measurement":10},
    {"Recipe":"R1","Tool":"T1","measurement":np.nan},
    {"Recipe":"R1","Tool":"T1","measurement":30},
]
count=2, mean=20
"""
import numpy as np
import pandas as pd


def recipe_tool_group_stats(df: pd.DataFrame):
    columns = ["Recipe", "Tool", "measurement"]
    if df.empty or any(column not in df.columns for column in columns):
        return None
    if not pd.api.types.is_numeric_dtype(df["measurement"]):
        return None

    # 全 NaN 组保留分组，并将其 p95 设为 NaN
    def p95(values):
        values = values.dropna()
        return np.percentile(values, 95) if not values.empty else np.nan

    stats = df.groupby(["Recipe", "Tool"])["measurement"].agg(
        count="count", mean="mean", std="std", p95=p95
    )
    return stats[["count", "mean", "std", "p95"]]
