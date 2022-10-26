import pandas as pd

def solution():
    df = pd.read_table('./popular-names.txt', header=None, sep='\t', names=['name', 'sex', 'number', 'year'])

    col1 = df['name']
    col1.to_csv('./col1.txt', index=False)
    print(col1.head())

    col2 = df['sex']
    col2.to_csv('./col2.txt', index=False)
    print(col2.head())
    
def main():
    solution()

if __name__ == "__main__":
    main()
