from pandas import read_excel, DataFrame, ExcelFile
def Read_Excel(path:str):
    file = ExcelFile(path)
    sheets = file.sheet_names
    df = file.parse(sheets[0])
    df_cleaned = df.loc[df.first_valid_index():].dropna(axis=1)
    if df.equals(df_cleaned):
        return df
    else:
        df_cleaned.columns = df_cleaned.iloc[0].to_list()
        df_cleaned = df_cleaned.iloc[1:]
        return df_cleaned.reset_index(drop=True)

