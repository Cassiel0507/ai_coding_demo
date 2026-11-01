"""
题目7：数据长度检查
【输入】
X：数组（list / numpy array 均可）
Y：数组（list / numpy array 均可）
recipes：数组（list / numpy array 均可）
tools：数组（list / numpy array 均可）
【输出】bool
- 四个数组长度完全相等 → 返回 True
- 任意一个长度不一样 → 返回 False
【异常约定】
- 不主动捕获异常；如果传入不是可求长度的对象（如int），触发原生异常，函数不做特殊处理
【验收标准】
1. 4个长度全部一致 → True
2. X和其他不一致 → False
3. Y和其他不一致 → False
4. recipes和其他不一致 → False
5. tools和其他不一致 → False
6. 支持普通Python list；支持numpy数组（使用len会兼容numpy数组shape[0]的校验逻辑）
"""
def check_data(X, Y, recipes, tools):
    # 四组数据长度一致时返回 True
    return len(X) == len(Y) == len(recipes) == len(tools)
