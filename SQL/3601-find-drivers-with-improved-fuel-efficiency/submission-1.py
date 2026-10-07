import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['fuel_eff'] = trips['distance_km'] / trips['fuel_consumed']
    df1 = trips[trips.trip_date < '2023-07-01']
    df2 = trips[trips.trip_date > '2023-06-30']

    df1 = df1.groupby(by='driver_id').agg(
        first_half_avg = ('fuel_eff', 'mean')
    ).reset_index()

    df2 = df2.groupby(by='driver_id').agg(
        second_half_avg = ('fuel_eff', 'mean')
    ).reset_index()

    df = df1.merge(df2, on='driver_id', how='left')
    df = df.merge(drivers, on='driver_id', how='left')

    df['efficiency_improvement'] = (df['second_half_avg'] - df['first_half_avg']).round(2)
    df = df[df.efficiency_improvement > 0]
    df['first_half_avg'] = df['first_half_avg'].round(2)
    df['second_half_avg'] = df['second_half_avg'].round(2)

    return df[['driver_id', 'driver_name', 'first_half_avg', 'second_half_avg', 'efficiency_improvement']].sort_values(by='efficiency_improvement', ascending=False)