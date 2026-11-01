"""
需求：题目5 验证候选工艺参数
函数：validate_candidate(X, Y, candidate, radius)

【输入】
X: np.ndarray，二维数组，shape = (样本数, 特征维度)，历史工艺特征
Y: np.ndarray，一维数组，shape = (样本数,)，对应的目标响应值
candidate: np.ndarray，一维数组，shape = (特征维度,)，待验证候选参数点
radius: float，每个维度的单侧搜索半径，>=0

【处理步骤顺序】
1. 校验维度对齐：X的特征维度必须等于candidate长度；X样本数量必须等于Y长度
2. 校验radius：radius < 0 → 抛 ValueError
3. 筛选规则：每个特征维度上，样本满足 candidate[d] - radius ≤ X[i,d] ≤ candidate[d] + radius
   必须**全部维度同时满足**才是命中样本
4. 收集命中样本对应的Y值
5. 如果没有命中样本：返回元组 (0, None)
6. 如果存在命中样本：返回 (命中数量, 命中样本Y的均值)，均值为float

【异常约定】
- X / Y / candidate 不是 np.ndarray → TypeError
- X是一维数组 → ValueError（必须二维）
- Y不是一维数组 → ValueError
- candidate不是一维数组 → ValueError
- X.shape[0] != Y.shape[0] 样本数不匹配 → ValueError
- X.shape[1] != candidate.shape[0] 特征维度不匹配 → ValueError
- radius 小于0 → ValueError
- X、Y、candidate内出现非数值（NaN/Inf）：不主动拦截，按numpy比较逻辑正常判断

【验收标准（测试点）】
1. 有多条样本全部维度落在范围内，返回正确数量、Y均值
2. 部分样本只有个别维度落在区间，其他维度超出 → 不命中
3. 无任何样本满足全部维度条件 → 返回 (0, None)
4. radius=0：严格等于候选点才命中
5. 样本数为0（X是空二维数组）→ 返回 (0, None)
6. radius负数 → 抛 ValueError
7. X、Y样本数量不一致 → 抛 ValueError
8. candidate特征维度和X特征数不一致 → 抛 ValueError
9. X、Y、candidate类型传list → 抛 TypeError
"""
import numpy as np


def validate_candidate(X, Y, candidate, radius):
    # 输入类型校验
    if not isinstance(X, np.ndarray):
        raise TypeError("X must be a numpy.ndarray")
    if not isinstance(Y, np.ndarray):
        raise TypeError("Y must be a numpy.ndarray")
    if not isinstance(candidate, np.ndarray):
        raise TypeError("candidate must be a numpy.ndarray")

    # 结构校验
    if X.ndim != 2:
        raise ValueError("X must be 2D")
    if Y.ndim != 1:
        raise ValueError("Y must be 1D")
    if candidate.ndim != 1:
        raise ValueError("candidate must be 1D")
    if X.shape[0] != Y.shape[0]:
        raise ValueError("X and Y sample counts do not match")
    if X.shape[1] != candidate.shape[0]:
        raise ValueError("candidate dimension does not match X feature dimension")
    if radius < 0:
        raise ValueError("radius must be >= 0")

    # 仅当所有特征维度都在候选点 ± radius 范围内时，才认为命中
    mask = np.all((candidate - radius <= X) & (X <= candidate + radius), axis=1)
    hits = Y[mask]
    if hits.size == 0:
        return 0, None
    return hits.size, float(np.mean(hits))
