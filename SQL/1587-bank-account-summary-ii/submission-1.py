import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.groupby(by='account').agg(
        balance = ('amount', 'sum')
    ).reset_index()

    df = df[df.balance > 10000]

    df = df.merge(users, on='account', how='left')
    return df[['name', 'balance']]