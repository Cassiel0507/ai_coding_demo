"""
题目13：异常特征计数
需求描述：
给定4个FFT比值组成的列表 fft_ratios，4个包络谱比值组成的列表 env_ratios；
分别统计：fft_ratios 里面大于2的数量、env_ratios 里面大于2的数量。
再传入一个报警阈值 alarm_threshold：
如果【fft超标的数量 + 包络超标的数量 >= alarm_threshold】，报警标记返回 True，否则返回 False。
提示：使用 sum(r > 2 for r in ratios) 统计超标个数。

输入：
    fft_ratios: list[float]，必须恰好4个浮点数
    env_ratios: list[float]，必须恰好4个浮点数
    alarm_threshold: int，全局报警阈值（总超标数量阈值）

输出规则：
    返回元组 (fft_over_cnt: int, env_over_cnt: int, is_alarm: bool)

边界 & 异常约定：
    1. fft_ratios 长度不等于4 或者 env_ratios 长度不等于4 → 返回 None
    2. alarm_threshold 不是正整数（<=0）→ 返回 None
    3. 比值等于2：不算超标，只统计严格 > 2
    4. 比值可以是负数、0、小数，直接按数值比较
    5. 不校验列表内元素类型；如果里面不是数字，行为不做保证，调用方保证输入合法

验收用例清单（本需求配套）
用例1：正常，fft有2个>2，包络1个>2；阈值3，总和等于3 → 报警True
    fft=[2.1, 1.5, 3.0, 1.9], env=[1.0, 2.5, 2.0, 0.8], threshold=3
    fft_over=2, env_over=1, sum=3 → (2, 1, True)
用例2：总和小于阈值，不报警
    fft=[2.1,1.1,1.2,1.3], env=[1.4,1.5,1.6,1.7], threshold=3
    fft_over=1, env_over=0, sum=1 → (1,0,False)
用例3：全部刚好等于2，没有超标
    fft=[2,2,2,2], env=[2,2,2,2], threshold=1
    fft_over=0, env_over=0 → (0,0,False)
用例4：全部都大于2
    fft=[3,4,5,6], env=[2.2,2.3,2.4,2.5], threshold=5
    fft_over=4, env_over=4, sum=8 ≥5 → (4,4,True)
用例5：fft长度不是4 → 返回None
用例6：env长度不是4 → 返回None
用例7：阈值为0（非法）→ 返回None
用例8：包含负数比值，负数不会>2，不计入
    fft=[-1, -2, 2.5, 1.0], env=[2.1, -5, 0, 1.8], threshold=2
    fft_over=1, env_over=1 sum=2 → (1,1,True)
"""

def count_abnormal_features(fft_ratios, env_ratios, alarm_threshold):
    if (len(fft_ratios) != 4 or len(env_ratios) != 4
            or not isinstance(alarm_threshold, int)
            or isinstance(alarm_threshold, bool) or alarm_threshold <= 0):
        return None

    # 仅统计严格大于 2 的比值，再按总数判断是否报警
    fft_over_cnt = sum(ratio > 2 for ratio in fft_ratios)
    env_over_cnt = sum(ratio > 2 for ratio in env_ratios)
    is_alarm = fft_over_cnt + env_over_cnt >= alarm_threshold
    return fft_over_cnt, env_over_cnt, is_alarm
