import pandas as pd

def get_season(date):
    month = date.month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    df['is_weekend'] = df['ds'].dt.dayofweek.isin([5, 6]).astype(int)
    df['season'] = df['ds'].apply(get_season)
    season_dummies = pd.get_dummies(df['season'])
    df = pd.concat([df, season_dummies], axis=1)
    return df