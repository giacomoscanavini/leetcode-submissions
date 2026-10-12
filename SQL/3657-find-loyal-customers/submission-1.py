import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    df = customer_transactions.groupby(by='customer_id').agg(
        nRefunded = ('transaction_type', lambda x: (x == 'refund').sum()),
        nTotal = ('transaction_type', 'size'),
        firstActivity = ('transaction_date', 'min'),
        lastActivity = ('transaction_date', 'max'),
    ).reset_index()

    df['refunded_pct'] = df.nRefunded / df.nTotal
    df['nPurchase'] = df.nTotal - df.nRefunded
    df['activityPeriod'] = (pd.to_datetime(df['lastActivity']) - pd.to_datetime(df['firstActivity'])).dt.days

    df = df[(df.nPurchase >= 3) & (df.activityPeriod >= 30) & (df.refunded_pct < 0.2)]
    
    return df[['customer_id']].sort_values(by='customer_id', ascending=True)