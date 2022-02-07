#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def solution(s, t):
    index = 0
    ans = ""
    while(index < len(s)):
        ans += s[index]
        ans += t[index]
        index += 1
    return ans

def main():
    print(solution("パトカー", "タクシー"))

if __name__ == "__main__":
    main()