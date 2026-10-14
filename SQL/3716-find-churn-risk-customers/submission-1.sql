# Write your MySQL query statement below
WITH 
    Ranked AS (
        SELECT 
            user_id, 
            event_date, 
            event_type,
            plan_name,
            monthly_amount,
            ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY event_date DESC
            ) AS latest,
            LEAD(event_date, 1) OVER (
                PARTITION BY user_id
                ORDER BY event_date ASC
            ) AS next_event_date
        FROM Subscription_events
    ), 
    Historical AS (
        SELECT 
            user_id,
            SUM(IF(event_type = 'downgrade', 1, 0)) AS num_downgrade,
            MAX(monthly_amount) AS max_historical_amount
        FROM Subscription_events
        GROUP BY user_id
    ),
    Days AS (
        SELECT 
            user_id,
            CASE 
                WHEN event_type = 'cancel' THEN 0
                ELSE DATEDIFF(next_event_date, event_date)
            END AS days_as_subscriber
        FROM Ranked
    ),
    DaysSub AS (
        SELECT 
            user_id,
            SUM(days_as_subscriber) AS days_as_subscriber
        FROM Days
        GROUP BY user_id
    )

SELECT 
    r.user_id,
    r.plan_name AS current_plan,
    r.monthly_amount AS current_monthly_amount,
    h.max_historical_amount,
    d.days_as_subscriber
FROM Ranked r
JOIN Historical h ON r.user_id = h.user_id
LEFT JOIN DaysSub d ON r.user_id = d.user_id
WHERE
    r.latest = 1
    AND r.plan_name IS NOT NULL
    AND h.num_downgrade > 0
    AND r.monthly_amount / h.max_historical_amount < 0.5
    AND d.days_as_subscriber >= 60

ORDER BY d.days_as_subscriber DESC, r.user_id ASC