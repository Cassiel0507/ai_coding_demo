"""
题目10：频率区间筛选 + 区间内幅值RMS计算
依赖库：numpy

【输入】
freq: np.ndarray，一维数组，频率，单位Hz；长度和amp完全一致
amp: np.ndarray，一维数组，幅值；长度和freq完全一致

【逻辑规则】
1. 筛选条件：频率满足 0.02 ≤ freq ≤ 0.1 Hz
2. 取出该区间内对应的amp幅值数组
3. RMS计算公式：RMS = sqrt( mean( amp_selected ** 2 ) )

【输出】
selected_amp: np.ndarray，筛选出来落在0.02~0.1Hz区间内的幅值
rms_value: float，筛选幅值的RMS值

【异常约定】
1. 若freq、amp长度不一致 → 抛出 ValueError
2. 输入不是numpy一维数组 → 抛出 TypeError
3. 区间内没有任何数据（selected_amp为空）→ 返回空数组，rms_value返回np.nan，不抛异常

【验收标准】
1. 边界0.02 Hz、0.1 Hz 两个点要包含在内（闭区间）
2. 全部数值计算使用numpy运算，不用原生循环
3. 返回顺序固定：(selected_amp, rms_value)
"""
import numpy as np


def freq_range_rms(freq: np.ndarray, amp: np.ndarray):
    # 校验输入类型和对应数据长度
    if not isinstance(freq, np.ndarray) or not isinstance(amp, np.ndarray):
        raise TypeError("freq and amp must be numpy arrays")
    if freq.ndim != 1 or amp.ndim != 1:
        raise TypeError("freq and amp must be one-dimensional")
    if len(freq) != len(amp):
        raise ValueError("freq and amp must have the same length")

    # 按闭区间筛选，并计算筛选幅值的 RMS
    selected_amp = amp[(freq >= 0.02) & (freq <= 0.1)]
    if selected_amp.size == 0:
        return selected_amp, float(np.nan)
    return selected_amp, float(np.sqrt(np.mean(selected_amp ** 2)))
