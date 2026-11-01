"""
题目8：按照时间排序
【输入】
time：numpy数组，时间数值
current：numpy数组，电流数值
tools：numpy数组，工具标识字符串
约束：三个数组长度必须相同；均为一维numpy数组
【输出】
返回三个numpy数组：sorted_time, sorted_current, sorted_tools
排序规则：按time从小到大升序排序，time、current、tools的行索引对应关系保持不变
【异常约定】
1. 如果三个数组长度不一致，不做内部捕获，抛出原生numpy异常
2. 如果输入不是numpy数组，不做类型兼容，交给原生报错
3. 只处理一维数组，不额外兼容多维数组
【验收标准】
1. 示例输入 time=[300,100,200], current=[0.03,0.01,0.02], tools=['T3','T1','T2']
   排序后 time=[100,200,300], current=[0.01,0.02,0.03], tools=['T1','T2','T3']
2. time本身已经有序，返回和原数组一致
3. time存在相等值：相等时间的条目相对顺序稳定即可
4. 数组只有1个元素，原样返回三个数组
"""
import numpy as np


def sort_machine_data(time, current, tools):
    # 按时间稳定排序，并用相同索引保持数据对应关系
    order = np.argsort(time, kind="stable")
    return time[order], current[order], tools[order]
