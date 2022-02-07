import l03
# “Hi He Lied Because Boron Could Not Oxidize Flu orine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

def solution(s):
    lst = l03.solution(s)
    # print(lst)
    l1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    dic = {}
    str = ""
    for i in range(len(lst)):
        # 1 or 2文字取り出す
        if i + 1 in l1:
            str = lst[i][0:1]
            if lst[i][0] in dic:
                dic[str].append(i + 1)
            else:
                dic[str] = [i + 1]
        else:
            str = lst[i][0:2]
            if str in dic:
                dic[str].append(i + 1)
            else:
                dic[str] = [i + 1]

    return dic


def main():
    print(solution("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."))

if __name__ == "__main__":
    main()