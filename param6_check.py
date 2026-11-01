"""
需求：题目6 合并历史与最新模型结果
函数：merge_results(old_results, new_results)

【输入】
old_results: dict，key 是元组 (Recipe: str, Tool: str)，value 为模型结果（任意类型）
new_results: dict，key 是元组 (Recipe: str, Tool: str)，value 为模型结果（任意类型）

【处理步骤顺序】
1. 校验输入：old_results、new_results 必须都是字典
2. 合并规则：
   - 同时存在相同 (Recipe, Tool) 键：优先保留 new_results 的值（新覆盖旧）
   - 只在 old_results 存在的键：保留旧结果
   - 只在 new_results 存在的键：保留新结果
3. 输出：返回全新字典，不修改原始 old_results、new_results

【异常约定】
- old_results 或者 new_results 不是 dict → 抛出 TypeError
- 字典中的 key 不是长度为2的元组，元组内两个元素不是字符串 → 抛出 ValueError

【验收标准（测试点）】
1. 新旧存在相同(Recipe,Tool)组合：新值覆盖旧值
2. 旧字典独有key、新字典独有key：全部保留
3. old_results 是空字典：直接返回new_results的拷贝
4. new_results 是空字典：直接返回old_results的拷贝
5. 两个输入都为空字典：返回空字典
6. 输入不是dict（list、int）→ 抛 TypeError
7. key不是(字符串,字符串)二元组 → 抛 ValueError
"""
def merge_results(old_results, new_results):
    # 输入必须都是字典
    if not isinstance(old_results, dict) or not isinstance(new_results, dict):
        raise TypeError("old_results and new_results must be dicts")

    # 校验所有 key：必须是长度为 2 的元组，且两个元素都为字符串
    for name, results in [("old_results", old_results), ("new_results", new_results)]:
        for key in results:
            if not isinstance(key, tuple) or len(key) != 2:
                raise ValueError(f"{name} keys must be (Recipe, Tool) tuples")
            if not all(isinstance(item, str) for item in key):
                raise ValueError(f"{name} tuple keys must contain strings")

    # 合并：新值覆盖旧值，且返回新字典，不修改原始对象
    merged = dict(old_results)
    merged.update(new_results)
    return merged
