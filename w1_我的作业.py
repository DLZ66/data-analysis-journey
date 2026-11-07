# -*- coding: utf-8 -*-
"""
W1 作业：统计一个 CSV 的行数、缺失值数量
==================================================================
怎么用这个文件：
  1. 先别看 w1_参考答案.py
  2. 把下面 4 个 TODO 填掉
  3. 运行，看输出对不对
  4. 卡住 20 分钟以上，再去看参考答案，看完关掉，自己重写一遍

本文件第 1 步已经写好了，因为"怎么读文件"属于语法，不是作业本身。
你要写的是"数数"这部分逻辑。
"""

import csv
from pathlib import Path
from collections import Counter

DATA_PATH = Path(__file__).parent / "data" / "messy_sample.csv"

# 业务上算"没有值"的写法。你可以增删，但要能说出理由。
MISSING_TOKENS = {"", "-", "--", "n/a", "na", "null", "none", "待测", "未测"}


def load_rows(path: Path) -> list[list[str]]:
    """读 CSV，跳过全空行，去掉单元格首尾空格。"""
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if any(cell.strip() for cell in row):
                rows.append([cell.strip() for cell in row])
    return rows


# ------------------------------------------------------------------
# TODO 1：写一个函数 count_missing(header, body)，返回每列缺失个数
#   返回类型用 Counter（from collections import Counter，已导入）
#   提示：
#     - body 是"不含表头"的二维列表
#     - 遍历每一行，再遍历每个列下标 i
#     - 取值用 row[i]，但注意有些行可能比表头短 → 用 len(row) 判断
#     - 判断"是不是缺失"：把值转小写后看是不是在 MISSING_TOKENS 里
#     - 不要用 == 一串 or，用 in 集合
# ------------------------------------------------------------------
def count_missing(header, body):
    # 把你的代码写在这
    pass


# ------------------------------------------------------------------
# TODO 2：写 main()，打印
#     - 文件有几列
#     - 数据行数（不含表头！这是最容易错的地方）
#     - 每列缺失个数 + 占比（百分比，保留 1 位小数）
#   提示：占比 = 缺失数 / 行数 * 100
# ------------------------------------------------------------------
def main():
    rows = load_rows(DATA_PATH)
    header, body = rows[0], rows[1:]

    # 把你的代码写在这
    pass


if __name__ == "__main__":
    main()


# ------------------------------------------------------------------
# TODO 3（做完 1、2 再来看）：这个 CSV 有几行是重复的？
#   "重复"的定义你自己定：整行完全相同算重复？还是样品编号相同算重复？
#   两种都算一遍，看看结果差多少，然后把结论写进复盘。
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO 4（选做）：把结果同时写进 result.txt
#   提示：with open("result.txt", "w", encoding="utf-8") as f: ...
# ------------------------------------------------------------------
