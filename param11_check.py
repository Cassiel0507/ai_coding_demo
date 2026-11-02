"""
题目11：寻找频率峰值
需求描述：
给定一组频率-幅值数据点，在用户指定的频率区间 [freq_min, freq_max] 内，找到幅值最大的那一组，返回对应的频率和幅值。
如果区间内没有任何落在范围内的数据点，返回 None。

输入：
    freq_amp_data: list[tuple[float, float]]
        列表内每个元素是 (频率freq, 幅值amplitude)
    freq_min: float，区间下限（包含）
    freq_max: float，区间上限（包含）

输出规则：
    1. 区间内存在有效数据：返回元组 (peak_freq: float, peak_amp: float)
    2. 区间内无有效数据：返回 None
    3. 多个点幅值同为最大值：返回第一个遇到的最大幅值点

边界 & 异常约定：
    1. freq_min > freq_max：视作非法区间，返回 None
    2. freq_amp_data 为空列表：返回 None
    3. 幅值可以是负数，比较大小按原始数值比较
    4. 频率刚好等于 freq_min / freq_max：算落在区间内
    5. 不做类型校验：调用方保证输入类型正确，不额外处理字符串等错误类型输入

验收用例清单（本需求配套）
用例1：正常情况，区间内存在多个点，取幅值最大
    data = [(10, 2.2), (20, 5.5), (30, 3.1)], min=10, max=30 → (20,5.5)
用例2：区间内无数据
    data = [(10, 2.2), (20, 5.5)], min=30, max=50 → None
用例3：多个点幅值相等，取第一个最大值
    data = [(10, 4.0), (20, 4.0)], min=10, max=20 → (10,4.0)
用例4：freq_min > freq_max 反向区间 → None
用例5：原始数据是空列表 → None
用例6：边界点刚好等于上下限
    data = [(5, 1.1), (10, 9.9)], min=10, max=10 → (10,9.9)
用例7：幅值含负数，选里面相对最大
    data = [(1, -5), (2, -1)], min=1, max=2 → (2, -1)
"""

def find_freq_peak(freq_amp_data, freq_min, freq_max):
    if freq_min > freq_max:
        return None

    peak = None
    # 仅在闭区间内更新最大值；相等时保留先出现的数据点
    for freq, amp in freq_amp_data:
        if freq_min <= freq <= freq_max and (peak is None or amp > peak[1]):
            peak = (freq, amp)
    return peak
