# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

def solution(s):
    return s[0] + s[2] + s[4] + s[6]

def main():
    print(solution("パタトクカシーー"))

if __name__ == "__main__":
    main()