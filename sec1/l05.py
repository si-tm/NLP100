import l03
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
# n-gram 参照 : https://mojitoba.com/2019/09/23/what-is-ngram/

def n_gram(lst, n):
    ans_lst = []
    for i in range(len(lst) - n + 1):
        str = []
        for j in range(n):
            str.append(lst[i + j])
        ans_lst.append(str)
    return ans_lst

# 単語n-gram
def solution_word(s, n):
    lst = l03.solution(s)
    return n_gram(lst, n)

#文字n-gram
def solution_letter(s, n):
    lst_w = l03.solution(s)
    lst_l = []
    for l in lst_w:
        for i in range(len(l)):
            lst_l.append(l[i])
    return n_gram(lst_l, n)

def main():
    print(solution_word("I am an NLPer", 2))
    print(solution_letter("I am an NLPer", 2))

if __name__ == "__main__":
    main()