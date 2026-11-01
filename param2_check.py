"""
需求：题目2 筛选重要特征 Top-3
函数：get_top_features(importance)

【输入】
importance: dict，key=特征名字（字符串），value=特征重要性分数（float）
约定：分数可以是正数、0、负数；value 只允许数字类型（int/float）；字典可以为空。

【输出规则】
1. 过滤：只保留 分数 > 0.1 的特征
2. 排序：按重要性分数【降序】排列
3. 截取：取排序后的前3个特征名称，返回 list[str]
4. 如果满足条件的特征不足3个，有多少返回多少；没有符合条件的返回空列表

【异常约定】
- 如果输入不是字典：直接抛出 TypeError
- 如果字典里某个 value 不是 int / float：抛出 TypeError

【验收标准（测试点）】
1. 正常情况：超过3个符合条件，返回分数最高的3个特征名，降序
2. 刚好3个符合条件：全部返回，降序
3. 少于3个符合条件：全部返回
4. 全部分数 <=0.1：返回空列表
5. 存在负数分数：直接过滤掉
6. 空字典输入：返回空列表
7. 输入不是dict（list/None）：抛 TypeError
8. dict内包含非数字value（字符串）：抛 TypeError
"""
def get_top_features(importance):
    if not isinstance(importance, dict):
        raise TypeError("importance must be a dict")

    # 校验所有分数，避免无效值被筛选条件跳过。
    if any(not isinstance(score, (int, float)) for score in importance.values()):
        raise TypeError("feature importance scores must be numeric")

    return [
        name
        for name, score in sorted(
            importance.items(), key=lambda item: item[1], reverse=True
        )
        if score > 0.1
    ][:3]
