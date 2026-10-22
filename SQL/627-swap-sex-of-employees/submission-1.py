import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    def change_sex(x):
        if x == 'm': return 'f'
        else: return 'm'
    
    salary['sex'] = salary['sex'].apply(change_sex)
    
    # salary["sex"] = salary["sex"].map({"m": "f", "f": "m"})
    # salary["sex"].replace({"f": "m", "m": "f"}, inplace=True)
    return salary