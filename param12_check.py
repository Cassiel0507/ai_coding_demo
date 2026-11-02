"""
题目12：谐波幅值提取
需求描述：
给定基频 f1，频率数组 freq（一维numpy数组）、对应的幅值数组 amp（一维numpy数组），
分别定位 2*f1、3*f1、4*f1 这三个目标谐波频率；
对每个目标频率，在 freq 数组里找到距离它最近的频率点，取出对应幅值；
按顺序返回 [二次谐波幅值，三次谐波幅值，四次谐波幅值]。
提示：使用 np.argmin(np.abs(freq - target)) 寻找下标。

输入：
    f1: float，基频
    freq: np.ndarray，一维，频率序列
    amp: np.ndarray，一维，幅值序列，长度必须和 freq 一致

输出规则：
    成功匹配：返回 list[float] = [amp_2f, amp_3f, amp_4f]

边界 & 异常约定：
    1. freq 和 amp 长度不一致：返回 None
    2. freq 为空数组 / amp 为空数组：返回 None
    3. freq、amp 不是一维数组：返回 None
    4. f1 <= 0（基频非法）：返回 None
    5. 目标谐波频率 2f1/3f1/4f1 可以超出 freq 的范围，依然取 freq 里离它最近的点
    6. 多个频率与目标距离相等：np.argmin 取下标更小的那一个
    7. 不校验 freq 是否升序；不做插值，只取现有离散点的幅值
    8. 不处理非numpy数组输入；调用方传入非np数组视为非法输入，返回 None

验收用例清单（本需求配套）
用例1：标准正常场景，谐波点都在频谱区间内
    f1=10, freq=np.array([5,10,20,30,40,50]), amp=np.array([0.1, 1.0, 0.8, 0.6, 0.4, 0.2])
    target:20,30,40 → 输出 [0.8, 0.6, 0.4]
用例2：谐波目标超出频谱右端，取最后一个最近点
    f1=20, freq=np.array([10,20,30]), amp=np.array([1,2,3])
    target:40,60,80，都大于30，都匹配30 → 输出 [3,3,3]
用例3：谐波目标小于最小频率，取第一个点
    f1=1, freq=np.array([10,20,30]), amp=np.array([5,6,7])
    target:2,3,4，都小于10 → 输出 [5,5,5]
用例4：距离相等，取下标靠前的点
    f1=10, freq=np.array([18,22,30,34,40,44]), amp=np.array([10,20,30,40,50,60])
    2f1=20，离18、22距离相同，取18；3f1=30精准命中；4f1=40精准命中 → [10,30,50]
用例5：freq和amp长度不一样 → 返回 None
用例6：f1<=0，f1=0或者f1=-5 → 返回 None
用例7：freq空数组 → 返回 None
"""
import numpy as np


def extract_harmonic_amplitude(f1, freq, amp):
    if (not isinstance(freq, np.ndarray) or not isinstance(amp, np.ndarray)
            or freq.ndim != 1 or amp.ndim != 1
            or freq.size == 0 or amp.size == 0
            or freq.size != amp.size or f1 <= 0):
        return None

    # 为 2、3、4 倍基频分别选取最近频点的幅值
    return [
        float(amp[np.argmin(np.abs(freq - multiple * f1))])
        for multiple in (2, 3, 4)
    ]
