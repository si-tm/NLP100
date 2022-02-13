# 行数をカウントせよ 確認にはwcコマンドを用いよ
# wc popular-names.txt 
# 2780   11120   55026 popular-names.txt

def solution(f):
    return sum([1 for _ in open(f)])

def main():
    print(solution("popular-names.txt"))

if __name__ == "__main__":
    main()