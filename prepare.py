import pandas as pandas

def percent_of_values_missing(df):
    return round(df.isna().sum()/len(df)*100,2)

def prep_belong():
    df.drop(column='belongs_to_collection', inplaxce=True)
    return df

def prep_homepage():
    df.drop(column='homepage', inplace=True)
    return df

def prep_tagline():
    df.tagline.fillna('None', inplace=True)
    return df

def prep_missing():
    df = df.dropna()


def prepare_data(df):
    prep_belong()
    prep_homepage()
    prep_tagline()
    prep_missing()
    return df                    