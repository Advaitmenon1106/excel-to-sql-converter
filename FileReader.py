from pandas import read_excel, DataFrame, ExcelFile, read_csv

def read_file(path:str):
    if '.csv' in path:
        df = read_csv(path)
        return df
    
    file = ExcelFile(path)
    sheets = file.sheet_names
    tables_raw = []
    for i in sheets:
        tables_raw.append(file.parse(i))
    return tables_raw
    
def clean_dataframe(df:DataFrame):
    df_cleaned = df.loc[df.first_valid_index():].dropna(axis=1)
    if df.equals(df_cleaned):
        return df
    else:
        df_cleaned.columns = df_cleaned.iloc[0].to_list()
        df_cleaned = df_cleaned.iloc[1:]
        return df_cleaned.reset_index(drop=True)
