import pandas as pd

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    graph = defaultdict(list)
    levels, teams, budgets = defaultdict(int), defaultdict(int), defaultdict(int)
    
    def dfs(manager: int, lev: int) -> None:
        levels[manager] = lev
        
        for employee in graph[manager]:
            dfs(employee, lev+1)
            teams[manager] += teams[employee]+1
            budgets[manager] += budgets[employee]

    ceo = employees.loc[employees["manager_id"].isnull(), "employee_id"][0]

    for manager, employee, salary in zip(employees["manager_id"], employees["employee_id"], employees["salary"]):
        graph[manager].append(employee)
        budgets[employee] = salary

    dfs(ceo, 1)

    employees["level"] = employees["employee_id"].apply(lambda x: levels[x])
    employees["team_size"] = employees["employee_id"].apply(lambda x: teams[x])
    employees["budget"] = employees["employee_id"].apply(lambda x: budgets[x])

    return employees[["employee_id","employee_name","level","team_size","budget"]].sort_values(["level","budget","employee_name"], ascending=[True, False, True])