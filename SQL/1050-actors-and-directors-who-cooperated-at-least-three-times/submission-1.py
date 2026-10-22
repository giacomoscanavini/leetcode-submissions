import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(by=['actor_id', 'director_id']).agg(
        nTimes = ('timestamp', 'count')
    ).reset_index()

    df = df[df.nTimes >= 3]

    return df[['actor_id', 'director_id']]