import pandas as pd

def solution():
    df = pd.read_table('./popular-names.txt', header=None, sep='\t', names=['name', 'sex', 'number', 'year'])
    N = input('>> ')
    print(df.head(int(N)))
    
def main():
    solution()

if __name__ == "__main__":
    main()
