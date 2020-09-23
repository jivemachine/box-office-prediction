import pandas as pandas

def percent_of_values_missing(df):
    return round(df.isna().sum()/len(df)*100,2)

def prep_belong(df):
    df.drop(columns='belongs_to_collection', inplace=True)
    return df

def prep_homepage(df):
    df.drop(columns='homepage', inplace=True)
    return df

def prep_tagline(df):
    df.tagline.fillna('None', inplace=True)
    return df

def prep_overview(df):
    df.overview.fillna("None", inplace=True)
    return df


def prep_production_companies(df):
    df.production_companies.fillna("Missing", inplace=True)
    return df

def prep_production_countries(df):
    df.production_countries.fillna('None', inplace=True)
    return df

def prep_runtime(df):
    df = df.dropna()   
    return df 

def prep_genres(df):
    df.genres.dropna(inplace=True)
    return df

def prep_spoken(df):
    df.spoken_languages.dropna(inplace=True)
    return df    

def prep_cast(df):
    df.cast.dropna(inplace=True)
    return df

def prep_crew(df):
    df.crew.dropna(inplace=True)
    return df

def prep_Keywords(df):
    df = df.drop(columns='Keywords', inplace=True)
    return df

def prepare_data(df):
    prep_belong(df)
    prep_homepage(df)
    prep_tagline(df)
    prep_overview(df)
    prep_production_companies(df)
    prep_production_countries(df)
    prep_runtime(df)
    prep_genres(df)
    prep_spoken(df)
    prep_cast(df)
    prep_crew(df)
    prep_Keywords(df)
    return df                    