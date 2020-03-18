from collections import deque
import math


def cell_inversion(n, string):
    """https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_c"""

    stack = deque()
    combination = 1

    for s in string:
        if len(stack) <= 0:
            if s != 'B':
                # 両端は'B'であるべき
                return 0
            stack.append(s)
        elif stack[-1] != s:
            # スタックの一番上と異なるならばスタックに追加する
            stack.append(s)
        else:
            # スタックにデータがあり、一番上とsが同じ値
            stack.pop()
            combination *= len(stack) + 1

    if len(stack) > 0:
        # スタックに値が残っていれば解が存在しない
        return 0

    # ペアの並び順をかけてreturn
    return combination * math.factorial(n)


def main():
    print(cell_inversion(4, 'BWBBWWWB')) # 288
    print(cell_inversion(3, 'BBWWBB'))  # 0
    print(cell_inversion(4, 'BWBWWWWB')) # 0


if __name__ == '__main__':
    main()
