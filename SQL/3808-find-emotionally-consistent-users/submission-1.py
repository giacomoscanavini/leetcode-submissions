import pandas as pd

def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:
    def ratio(x):
        dom_reaction = x.value_counts().idxmax()
        return (x.value_counts().loc[dom_reaction] / x.value_counts().sum() + 1e-6).round(2)

    df = reactions.groupby(by='user_id').agg(
        nReactions = ('content_id', 'nunique'),
        dominant_reaction = ('reaction', lambda x: x.mode().iloc[0]),
        reaction_ratio = ('reaction', ratio)
    ).reset_index()

    df = df[(df.nReactions >= 5) & (df.reaction_ratio >= 0.6)]
    df = df.drop(columns={'nReactions'})

    return df.sort_values(by=['reaction_ratio', 'user_id'], ascending=[False, True])