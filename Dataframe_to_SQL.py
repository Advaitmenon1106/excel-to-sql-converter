from FileReader import clean_dataframe, read_file


def generate_sql(path):
    tables = read_file(path=path)
    if type(tables) == list:
        cleaned_tables = []
        for df in tables:
            cleaned_tables.append(clean_dataframe(df=df))
    else:
        cleaned_df = clean_dataframe(tables)
    
