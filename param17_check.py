"""
题目17：提取Top3重要特征
需求描述：
传入特征名称列表、对应的重要性分数列表；
将特征与分数配对，按重要性分数从高到低降序排序；
返回排序后前3个特征的名称组成的列表。

输入：
    feature_names: list[str]，特征名称
    importances: list[float]，对应特征的重要性分数

输出规则：
    返回 list[str]，最多3个元素，按分数降序；
    不足3个特征时，有多少返回多少；
    分数相同：保留原列表先后顺序（稳定排序）

边界 & 异常约定：
    1. feature_names 和 importances 长度不一致 → 返回 None
    2. 任意一个列表为空，但另一个不为空 → 返回 None
    3. 两个都为空列表 → 返回空列表 []
    4. 分数允许负数、0，直接按数值大小比较
    5. 不校验列表内部元素类型，调用方保证输入合法

验收用例清单（本需求配套）
用例1：超过3个特征，正常取top3
names = ["f1","f2","f3","f4"], imp = [0.5, 0.2, 0.7, 0.1]
排序：f3(0.7), f1(0.5), f2(0.2), f4(0.1) → ["f3","f1","f2"]

用例2：一共只有2个特征，全部返回
names = ["a","b"], imp = [0.9,0.3] → ["a","b"]

用例3：分数相等，维持原有先后顺序
names = ["x","y","z"], imp = [0.6,0.6,0.2] → ["x","y","z"]

用例4：长度不匹配 → 返回 None
names = ["f1"], imp = [0.1,0.2]

用例5：两个列表都为空 → 返回 []

用例6：存在负的重要性分数
names = ["p","q","r"], imp = [-0.1, -0.5, 0.0]
排序：r(0.0), p(-0.1), q(-0.5) → ["r","p","q"]
"""

def get_top3_features(feature_names: list[str], importances: list[float]):
    if len(feature_names) != len(importances):
        return None

    # 稳定降序排序，分数相同则保留输入顺序
    ranked = sorted(zip(feature_names, importances), key=lambda item: item[1], reverse=True)
    return [name for name, _ in ranked[:3]]
