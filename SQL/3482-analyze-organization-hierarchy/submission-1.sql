# Write your MySQL query statement below
WITH 
    RECURSIVE Hierarchy AS (
        SELECT manager_id, employee_id, employee_name, salary, 1 AS level
        FROM Employees
        WHERE manager_id IS NULL

        UNION ALL

        SELECT e.manager_id, e.employee_id, e.employee_name, e.salary, level + 1 AS level
        FROM Employees e
        JOIN Hierarchy h ON e.manager_id = h.employee_id
    ), 
    Subordinate AS (
        SELECT manager_id, employee_id, salary
        FROM Employees

        UNION ALL

        SELECT s.manager_id, e.employee_id, e.salary
        FROM Employees e
        JOIN Subordinate s ON e.manager_id = s.employee_id
    )

SELECT 
    h.employee_id, h.employee_name, level, 
    COALESCE(COUNT(s.employee_id), 0) AS team_size,
    COALESCE(SUM(s.salary), 0) + h.salary AS budget
FROM Hierarchy h
LEFT JOIN Subordinate s ON h.employee_id = s.manager_id
GROUP BY h.employee_id, h.employee_name, level, h.salary
ORDER BY level ASC, budget DESC, employee_name ASC