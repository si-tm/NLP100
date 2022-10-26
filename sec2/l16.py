import pandas as pd

def split_file(N):
    tmp = df.reset_index(drop=False)
    df_cut = pd.qcut(tmp.index, N, labels=[i for i in range(N)])
    df_cut = pd.concat([df, pd.Series(df_cut, name='sp')], axis=1)

    return df_cut

def solution():
    df = pd.read_table('./popular-names.txt', header=None, sep='\t', names=['name', 'sex', 'number', 'year'])
    N = input('>> ')
    df_cut = split_file(int(N))
    df_cut['sp'].value_counts()
   

def main():
    solution()

if __name__ == "__main__":
    main()
