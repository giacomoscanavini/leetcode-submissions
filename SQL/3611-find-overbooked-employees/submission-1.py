import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    meetings['week'] = pd.to_datetime(meetings['meeting_date']).dt.to_period('W-SUN')

    df = meetings.groupby(by=['employee_id', 'week']).agg(
        meeting_heavy_weeks = ('duration_hours', 'sum')
    ).reset_index()
    df['meeting_heavy_weeks'] = df['meeting_heavy_weeks'] / 40
    df = df[df.meeting_heavy_weeks > 0.5]
    df = df.groupby(by='employee_id').agg(
        meeting_heavy_weeks = ('meeting_heavy_weeks', 'count')
    ).reset_index()
    df = df[df.meeting_heavy_weeks >= 2]
    
    df = df.merge(employees, on='employee_id', how='left')

    return df[['employee_id', 'employee_name', 'department', 'meeting_heavy_weeks']].sort_values(by=['meeting_heavy_weeks', 'employee_name'], ascending=[False, True])