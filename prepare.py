import pandas as pandas

def percent_of_values_missing(df):
    return round(df.isna().sum()/len(df)*100,2)