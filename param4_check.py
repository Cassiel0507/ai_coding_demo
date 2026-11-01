"""
需求：题目4 按设备和Recipe分组统计
函数：summarize(df)

【输入】
df: pandas.DataFrame
必须包含3列：ToolName（设备名称，字符串）、RECIPE_NAME（配方名，字符串）、ImplantCurrent（注入电流，数值int/float）
允许ImplantCurrent存在NaN；ToolName、RECIPE_NAME不允许NaN（业务约定）

【处理步骤顺序】
1. 校验输入列：缺少上面任意一列 → 抛出 ValueError
2. 过滤：ImplantCurrent为NaN的行直接丢弃，不参与统计
3. 分组：按 ToolName + RECIPE_NAME 两列联合分组
4. 分组聚合：
   - count: 本组有效样本行数（ImplantCurrent非空）
   - mean_current: 本组ImplantCurrent平均值
5. 输出：返回新DataFrame
   索引：ToolName, RECIPE_NAME（多层索引）
   列：["count", "mean_current"]
   保持分组顺序不做强制排序

【异常约定】
- 输入不是pandas DataFrame → 抛出 TypeError
- 缺少 ToolName / RECIPE_NAME / ImplantCurrent 任一必填列 → 抛出 ValueError
- ToolName 或 RECIPE_NAME 存在NaN → 抛出 ValueError

【验收标准（测试点）】
1. 正常数据，多设备+多recipe，部分ImplantCurrent为NaN，正确分组计数、求均值
2. 某一组全部ImplantCurrent是NaN → 该组被直接剔除，不出现在结果里
3. 输入df为空（0行）→ 返回空的目标结构DataFrame（多层索引、两列）
4. 缺少必填列 → 抛 ValueError
5. ToolName / RECIPE_NAME 里面有NaN → 抛 ValueError
6. 输入不是DataFrame（list、dict）→ 抛 TypeError
"""
import pandas as pd


def summarize(df):
    # 输入必须是 DataFrame，且包含必填列
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    required_cols = ["ToolName", "RECIPE_NAME", "ImplantCurrent"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"missing required columns: {missing}")

    # ToolName / RECIPE_NAME 不能出现缺失值
    if df["ToolName"].isna().any() or df["RECIPE_NAME"].isna().any():
        raise ValueError("ToolName and RECIPE_NAME cannot contain NaN")

    # 删除 ImplantCurrent 为空的样本后按设备+配方分组统计
    valid = df.dropna(subset=["ImplantCurrent"])
    result = (
        valid.groupby(["ToolName", "RECIPE_NAME"], sort=False)
        .agg(count=("ImplantCurrent", "size"), mean_current=("ImplantCurrent", "mean"))
    )
    return result
