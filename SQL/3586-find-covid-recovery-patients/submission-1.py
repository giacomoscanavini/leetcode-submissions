import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    df = covid_tests.merge(covid_tests, on='patient_id', how='inner')
    df = df[(df.test_date_x < df.test_date_y) & (df.result_x == 'Positive') & (df.result_y == 'Negative')]
    df = df.groupby(by='patient_id').agg(
        min_pos = ('test_date_x', 'min'),
        min_neg = ('test_date_y', 'min')
    ).reset_index()

    df['recovery_time'] = (pd.to_datetime(df['min_neg']) - pd.to_datetime(df['min_pos'])).dt.days
    df = df.merge(patients, on='patient_id', how='left')

    return df[['patient_id', 'patient_name', 'age', 'recovery_time']].sort_values(by=['recovery_time', 'patient_name'], ascending=[True, True])