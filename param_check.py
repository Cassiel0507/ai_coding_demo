"""
需求分析
功能：工艺参数完整性检查
函数：find_missing_params(required_params, input_params)
输入：
    required_params: dict，必须要有的参数字典，key是参数名
    input_params: dict，用户传入的参数字典
输出：list，所有【在required_params里存在、但是input_params里面没有的key】
异常情况：
    输入不是字典时，暂时先返回空列表（或者我们后面再扩展，本次基础版先简单处理）
验收标准：
    示例1：
        required_params = {"temp":100, "pressure":0.5, "time":10}
        input_params = {"temp":90, "time":12}
        预期返回：["pressure"]
    示例2：全部参数齐全，返回 []
    示例3：一个都没传，返回全部required的key列表
"""
# 下面是题目给的起始代码
def find_missing_params(required_params, input_params):
    # 非字典输入返回空列表。
    if not isinstance(required_params, dict) or not isinstance(input_params, dict):
        return []

    return [key for key in required_params if key not in input_params]
