"""
题目18：新旧批次结果合并（Recipe, Tool 复合键）
需求描述：
旧批次结果 old_dict、新批次结果 new_dict；字典的 key 是元组 (Recipe, Tool)，value 是该分组的分析结果（任意类型）。
合并规则：
1. 以 (Recipe, Tool) 为唯一键；
2. 新批次里存在的键，覆盖旧批次同键的值；
3. 只在旧批次存在、新批次没有的键，保留旧值；
4. 只在新批次存在、旧批次没有的键，作为新增。
输出：返回元组 (merged_dict, count_new, count_updated, count_unchanged)
count_new：仅新字典有、旧字典没有的键数量
count_updated：新旧都存在，被新值覆盖的键数量
count_unchanged：仅旧字典有、新字典没有，保留原值的键数量

输入：
    old_dict: dict[tuple[str, str], any]
    new_dict: dict[tuple[str, str], any]

输出规则：
    merged_dict: 合并完成后的字典
    count_new: int，新增分组数
    count_updated: int，被更新覆盖分组数
    count_unchanged: int，保留旧数据分组数

边界 & 异常约定：
    1. old_dict、new_dict 不是字典类型 → 返回 None
    2. 不校验字典内 value 的类型，value 可以是数字、字典、列表等任意内容
    3. 键必须是 (Recipe, Tool) 二元字符串元组；函数不校验键格式，调用方保证输入合规
    4. value 相等与否不影响更新计数：只要新旧都存在同一个 key，一律算作 updated，不管值是不是一样
    5. 空字典合法，可以正常参与合并统计

验收用例清单（本需求配套）
用例1：混合新增、更新、保留
old = {("R1","T1"):10, ("R1","T2"):20, ("R2","T1"):30}
new = {("R1","T1"):99, ("R1","T3"):40}
merged：
("R1","T1") →99，("R1","T2")→20，("R2","T1")→30，("R1","T3")→40
count_new=1，count_updated=1，count_unchanged=2

用例2：new为空字典，全部保留旧数据
old = {("R1","T1"):5}
new = {}
count_new=0，count_updated=0，count_unchanged=1

用例3：old为空字典，全部是新增
old = {}
new = {("R1","T1"):7}
count_new=1，count_updated=0，count_unchanged=0

用例4：完全相同的key集合，全部更新
old = {("R1","T1"):1}
new = {("R1","T1"):2}
count_new=0，count_updated=1，count_unchanged=0

用例5：输入不是字典 → 返回 None
"""

def merge_recipe_tool_result(old_dict, new_dict):
    if not isinstance(old_dict, dict) or not isinstance(new_dict, dict):
        return None

    # 统计键的新增、更新与保留，并让新数据覆盖旧值
    count_new = len(new_dict.keys() - old_dict.keys())
    count_updated = len(new_dict.keys() & old_dict.keys())
    count_unchanged = len(old_dict.keys() - new_dict.keys())
    merged_dict = {**old_dict, **new_dict}
    return merged_dict, count_new, count_updated, count_unchanged
