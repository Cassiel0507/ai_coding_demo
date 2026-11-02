"""
题目14：规则配置化
需求描述：
内置配置字典，保存两台设备 ADPOL01_2A、ADPOL01_2B 的特征阈值：
ADPOL01_2A：feat1_th=5.0，feat2_th=10.0
ADPOL01_2B：feat1_th=7.0，feat2_th=12.0
判断逻辑：当 feat1 > feat1_th 并且 feat2 > feat2_th 时返回 1（触发告警），否则返回 0。

输入：
    device_name: str，设备标识
    feat1: float，特征1数值
    feat2: float，特征2数值

输出规则：
    设备存在且满足双特征同时超阈值 → 返回 1
    设备存在，但不满足双条件 → 返回 0
    设备名称不在配置内 → 返回 0

边界 & 异常约定：
    1. 比较是严格大于 >，等于阈值不算触发告警
    2. feat1、feat2 可以为负数、0、小数，直接数值比较
    3. 输入非字符串的 device_name、非数字特征值，不做类型捕获，按调用合法输入处理
    4. 内置阈值写死在函数内部的嵌套配置字典中，外部不可传入阈值
    5. 使用 dict.get() 安全读取配置

验收用例清单（本需求配套）
用例1：ADPOL01_2A，feat1>5，feat2>10，双条件满足 → 返回1
    device="ADPOL01_2A", feat1=6, feat2=11
用例2：ADPOL01_2A，feat1超，feat2不超 → 返回0
    device="ADPOL01_2A", feat1=6, feat2=9
用例3：ADPOL01_2B，双特征同时超过阈值 → 返回1
    device="ADPOL01_2B", feat1=8, feat2=13
用例4：ADPOL01_2B，刚好等于阈值，不触发 → 返回0
    device="ADPOL01_2B", feat1=7, feat2=12
用例5：设备不在配置表里（ADPOL99）→ 返回0
    device="ADPOL99", feat1=100, feat2=200
用例6：ADPOL01_2A，feat2超、feat1不足 → 返回0
    device="ADPOL01_2A", feat1=4, feat2=15
用例7：特征为负数，不满足条件 → 返回0
    device="ADPOL01_2A", feat1=-1, feat2=-2
"""

def rule_check(device_name: str, feat1: float, feat2: float):
    thresholds = {
        "ADPOL01_2A": {"feat1_th": 5.0, "feat2_th": 10.0},
        "ADPOL01_2B": {"feat1_th": 7.0, "feat2_th": 12.0},
    }
    config = thresholds.get(device_name)
    if config is None:
        return 0

    # 两个特征都严格超过对应阈值才触发告警
    return int(feat1 > config.get("feat1_th") and feat2 > config.get("feat2_th"))
