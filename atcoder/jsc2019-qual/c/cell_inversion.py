from collections import deque
import math


def cell_inversion(n, string):
    """https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_c"""

    # 右列かどうかを格納する
    is_right_list = [False] * (2 * n)
    stack = deque()
    for i, s in enumerate(string):
        # print(f'{i}, {s}')
        if len(stack) <= 0:
            if s != 'B':
                # 両端は'B'であるべき
                return 0
            # print(f'append:{s}')
            stack.append(s)
        elif stack[-1] != s:
            # スタックの一番上と異なるならばスタックに追加する
            # print(f'append:{s}')
            stack.append(s)
        else:
            # スタックにデータがあり、一番上とsが同じ値
            stack.pop()
            # print(f'popped')
            is_right_list[i] = True

    if len(stack) > 0:
        # スタックに値が残っていれば解が存在しない
        return 0

    # print(is_right_list)

    # 同じ左反転列が何通りあるのか
    right_count = 0
    combination = 1
    for is_right in is_right_list:
        if is_right:
            # 左側
            combination *= right_count
            right_count -= 1
        else:
            # 右がわ
            right_count += 1

    # ペアの並び順をかけてreturn
    return combination * math.factorial(n)


def main():
    print(cell_inversion(4, 'BWBBWWWB')) # 288
    print(cell_inversion(3, 'BBWWBB'))  # 0
    print(cell_inversion(4, 'BWBWWWWB')) # 0


if __name__ == '__main__':
    main()
