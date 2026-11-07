# -*- coding: utf-8 -*-
"""
W1 参考实现：统计一个 CSV 的行数与缺失值数量
------------------------------------------------------------------
只用 Python 标准库（csv / pathlib / collections），不依赖 pandas。
原因：pandas 安排在第 3 周。先用原生库把"读写文件"这件事搞明白，
      后面用 pandas 你才知道它替你做了什么。

运行方式（在当前目录下打开 PowerShell）：
    python w1_参考答案.py
"""

import csv
from pathlib import Path
from collections import Counter

# 用 __file__ 拼路径，这样不管在哪个目录运行都能找到数据文件
# （新手第一坑：写死 "data/messy_sample.csv" 然后在别的目录运行就报错）
DATA_PATH = Path(__file__).parent / "data" / "messy_sample.csv"

# 真实台账里，这些字符串其实都代表"没有值"。
# 注意：这一步是"业务判断"，不是技术判断 —— 你得问清楚"待测"算不算缺失。
MISSING_TOKENS = {"", "-", "--", "n/a", "na", "null", "none", "待测", "未测"}


def load_rows(path: Path) -> list[list[str]]:
    """读 CSV，返回二维列表。会做两件事：
    1) 跳过全空行（Excel 保存的文件末尾经常有）
    2) 去掉每个单元格首尾空格
    """
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        # encoding="utf-8-sig" 能同时处理"带 BOM"和"不带 BOM"的 UTF-8 文件。
        # 用 Excel 存过的 CSV 通常带 BOM，用普通 utf-8 读会多出一个 \ufeff 字符，
        # 第一个列名会变成 "\ufeff样品编号"，后面按列名匹配就全乱了。
        reader = csv.reader(f)
        rows = []
        for row in reader:
            # 全空行：每个格子都是空白 → 丢掉
            if any(cell.strip() for cell in row):
                rows.append([cell.strip() for cell in row])
    return rows


def count_missing(header: list[str], body: list[list[str]]) -> Counter:
    """逐列统计缺失个数。"""
    missing = Counter()
    for row in body:
        for i, col in enumerate(header):
            # 行长度不齐也是脏数据的一种：i 超出范围就当空值
            cell = row[i] if i < len(row) else ""
            if cell.lower() in MISSING_TOKENS:
                missing[col] += 1
    return missing


def main() -> None:
    rows = load_rows(DATA_PATH)
    if not rows:
        print("文件是空的")
        return

    header, body = rows[0], rows[1:]
    n = len(body)

    print("=" * 46)
    print(f"文件      ：{DATA_PATH.name}")
    print(f"列数      ：{len(header)}")
    print(f"数据行数  ：{n}   （不含表头）")
    print("=" * 46)

    missing = count_missing(header, body)
    print("\n各列缺失情况：")
    print(f"  {'列名':<10}{'缺失':>6}{'占比':>9}")
    print("  " + "-" * 26)
    for col in header:
        k = missing[col]
        rate = k / n * 100 if n else 0.0
        flag = "  <-- 缺失偏高" if rate >= 20 else ""
        print(f"  {col:<10}{k:>6}{rate:>8.1f}%{flag}")

    total_cells = n * len(header)
    total_missing = sum(missing.values())
    print("\n" + "=" * 46)
    print(f"缺失单元格：{total_missing} / {total_cells}"
          f"（总体缺失率 {total_missing / total_cells * 100:.1f}%）")
    print("=" * 46)


if __name__ == "__main__":
    main()


# ------------------------------------------------------------------
# 进阶任务（有余力再做，做完记进复盘）
# 1. 找出重复行：样品编号出现多次的有哪些？（提示：Counter 也能数这个）
# 2. 找出"数值列里混进单位"的：烧结温度列应有 "1250℃" 这种，怎么自动发现？
# 3. 找出异常值：温度出现 -999，强度出现 1203（千分位没处理），怎么筛？
# 4. 把结果写成一份 result.txt，而不是只打印到屏幕。
#
# 做完这四个，第 1 周就超额完成了。
# ------------------------------------------------------------------
