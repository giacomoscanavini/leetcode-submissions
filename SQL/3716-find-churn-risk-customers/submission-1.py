import pandas as pd

def find_churn_risk_customers(subscription_events: pd.DataFrame) -> pd.DataFrame:
    df = subscription_events.sort_values(by=['user_id', 'event_date'], ascending=[True, True])
    df['next_event_date'] = df.groupby(by='user_id')['event_date'].transform(lambda x: x.shift(-1))
    df['days'] = (pd.to_datetime(df['next_event_date']) - pd.to_datetime(df['event_date'])).dt.days
    flag = df['event_type'] != 'cancel'
    df['days'] = df['days'] * flag

    df1 = df.groupby(by='user_id').agg(
        max_historical_amount = ('monthly_amount', 'max'),
        num_downgrades = ('event_type', lambda x: (x == 'downgrade').sum()),
        days_as_subscriber = ('days', 'sum')
    ).reset_index()

    df2 = df[df.next_event_date.isna()]
    df2 = df2.merge(df1, on='user_id', how='left')

    df2 = df2[['user_id', 'plan_name', 'num_downgrades', 'monthly_amount', 'max_historical_amount', 'days_as_subscriber']]
    df2 = df2[(df2.plan_name.notna()) & (df2.num_downgrades > 0) & (df2.monthly_amount / df2.max_historical_amount < 0.5) & (df2.days_as_subscriber >= 60)]

    return (
        df2.drop(columns={'num_downgrades'})
        .rename(columns={'plan_name': 'current_plan', 'monthly_amount': 'current_monthly_amount'})
        .sort_values(by=['days_as_subscriber', 'user_id'], ascending=[False, True])
    )