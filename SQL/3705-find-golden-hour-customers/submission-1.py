import pandas as pd

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    restaurant_orders['peak_hour'] = (
        pd.to_datetime(restaurant_orders['order_timestamp'])
        .dt.hour
        .isin([11, 12, 13, 18, 19, 20]))

    df = restaurant_orders.groupby(by='customer_id').agg(
        total_orders = ('order_id', 'size'),
        num_peak_hour = ('peak_hour', 'sum'),
        num_rated = ('order_rating', lambda x: (x.notna()).sum()),
        average_rating = ('order_rating', 'mean'),
    ).reset_index()

    df['average_rating'] = df['average_rating'].round(2)
    df['peak_hour_percentage'] = (100 * df['num_peak_hour'] / df['total_orders']).round()

    flag_orders = df.total_orders >= 3
    flag_peak = df.peak_hour_percentage >= 60
    flag_avg_rating = df.average_rating >= 4
    flag_rated = df['num_rated'] / df['total_orders'] >= 0.5

    df = df[flag_orders & flag_peak & flag_avg_rating & flag_rated]

    return (
        df[['customer_id', 'total_orders', 'peak_hour_percentage', 'average_rating']]
        .sort_values(by=['average_rating', 'customer_id'], ascending=[False, False])
    )