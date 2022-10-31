import pandas as pd
#import sys


#my_file = sys.argv[1]

def process_data(input_file):
    df = pd.read_csv(input_file)
    return df


# run the app.
if __name__ == "__main__":
    df = process_data('foo.csv')
    print(df)
