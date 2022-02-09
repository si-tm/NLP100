# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# https://qiita.com/ell/items/6eb48e934a147898d823

def is_little_alphabet(c):
    if c >= 'a' and c <= 'z':
        return True
    return False

def solution(s):
    t = ""
    for i in range(len(s)):
        c = s[i]
        if is_little_alphabet(c):
            # (219 - 文字コード)の文字に置換
            new_c = chr(219 - ord(c))
            t += new_c
        else:
            t += c
    return t

def main():
    print(solution("susieは私の友達dayo"))

if __name__ == "__main__":
    main()