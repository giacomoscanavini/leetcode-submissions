# Write your MySQL query statement below
WITH Travelled AS (
    SELECT user_id, SUM(distance) AS travelled_distance
    FROM Rides
    GROUP BY user_id
)

SELECT u.name, COALESCE(t.travelled_distance, 0) AS travelled_distance
FROM Users u
LEFT JOIN Travelled t ON u.id = t.user_id
ORDER BY t.travelled_distance DESC, u.name ASC