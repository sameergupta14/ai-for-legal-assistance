import pandas as pd
import tokenize_to_counter


def extract_and_save(DIR_PATH):
    files = []
    for file in os.listdir(DIR_PATH):
        x = ""
        with open(os.path.join(DIR_PATH, file)) as f:
            for line in f.readlines():
                x += line
        files.append(x)
    extracted_data = pd.DataFrame()
    extracted_data["docs"] = files
    return extracted_data

def map_dataframe_to_counter(df):
    df["docs"] = df["docs"].apply(lambda x : tokenize_to_counter(x))
    return df

def solve(DIR_PATH):
    _data = map_dataframe_to_counter(extract_and_save(DIR_PATH))
    _data.to_csv("test_counters.csv")