import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby(by='player_id').agg(
        first_login = ('event_date', 'min')
    ).reset_index()

    return activity