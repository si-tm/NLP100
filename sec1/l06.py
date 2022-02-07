import l05
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def solution_sum(s, t):
    # XとYを作る
    X = set(l05.solution_letter_string(s, 2))
    Y = set(l05.solution_letter_string(t, 2))
    return X | Y

def solution_mult(s, t):
    # XとYを作る
    X = set(l05.solution_letter_string(s, 2))
    Y = set(l05.solution_letter_string(t, 2))
    return X & Y

def solution_diff(s, t):
    # XとYを作る
    X = set(l05.solution_letter_string(s, 2))
    Y = set(l05.solution_letter_string(t, 2))
    return X - Y

def main():
    print(solution_sum("paraparaparadise", "paragraph"))
    print(solution_mult("paraparaparadise", "paragraph"))
    print(solution_diff("paraparaparadise", "paragraph"))

if __name__ == "__main__":
    main()