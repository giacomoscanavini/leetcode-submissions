import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = rides.groupby(by='user_id').agg(
        travelled_distance = ('distance', 'sum')
    ).reset_index()

    df = users.merge(df, left_on='id', right_on='user_id', how='left')
    df = (
        df[['name', 'travelled_distance']]
        .fillna(0)
        .sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    )

    return df