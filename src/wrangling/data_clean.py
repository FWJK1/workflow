import pandas as pd


def clean_process_data():
    df = pd.read_csv("data/MOCK_DATA.csv")
    return df