import pandas as pd
import sys

def main():
    json = pd.read_json(sys.argv[1]).T
    
    for idx, row in json.iterrows():
        if row['label'] == 'fake':
            json.loc[idx]['label'] = 1
        else:
            json.loc[idx]['label'] = 0
    json.to_csv('dataset.csv')
    print(json)


if __name__ == "__main__":
    main()
