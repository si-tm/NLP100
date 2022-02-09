import l03
import random

# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，
# 長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，
# その実行結果を確認せよ．

def solution(s):
    l = l03.solution(s)
    ans = ""
    for s in l:
         # 4文字超なら
        if len(s) > 4:
            # 1からn-2までのリストを作成
            lst = list(range(1, len(s) - 2))
            random.shuffle(lst)
            print(lst)
            # 入れ替える
            ans += s[0]
            for i in range(len(lst)):
                ans += s[lst[i]]
            ans += s[-1]
        else:
            ans += s
        ans += " "
    return ans

def main():
    print(solution("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))

if __name__ == "__main__":
    main()