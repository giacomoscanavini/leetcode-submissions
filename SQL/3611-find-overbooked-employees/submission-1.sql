# Write your MySQL query statement below
WITH 
    Weeks AS (
        SELECT 
            employee_id, 
            YEARWEEK(meeting_date, 5) AS week_num, 
            duration_hours
        FROM Meetings
    ),
    Percentages AS (
        SELECT 
            employee_id,
            week_num,
            SUM(duration_hours) / 40 AS week_hours_pct
        FROM Weeks
        GROUP BY employee_id, week_num
        HAVING SUM(duration_hours) / 40 > 0.5
    ),
    MeetingHeavy AS (
        SELECT employee_id, COUNT(week_hours_pct) AS meeting_heavy_weeks
        FROM Percentages
        GROUP BY employee_id
        HAVING COUNT(week_hours_pct) >= 2
    )

SELECT m.employee_id, e.employee_name, e.department, m.meeting_heavy_weeks
FROM MeetingHeavy m
JOIN Employees e ON m.employee_id = e.employee_id
ORDER BY m.meeting_heavy_weeks DESC, e.employee_name ASC