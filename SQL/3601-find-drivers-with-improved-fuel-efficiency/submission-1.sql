# Write your MySQL query statement below
WITH 
    Fuels AS (
        SELECT *, distance_km / fuel_consumed AS fuel_eff
        FROM Trips
    ),
    FuelEarly AS (
        SELECT driver_id, AVG(fuel_eff) AS first_half_avg
        FROM Fuels 
        WHERE MONTH(trip_date) IN (1, 2, 3, 4, 5, 6)
        GROUP BY driver_id
        
    ),
    FuelLate AS (
        SELECT driver_id, AVG(fuel_eff) AS second_half_avg
        FROM Fuels 
        WHERE MONTH(trip_date) IN (7, 8, 9, 10, 11, 12)
        GROUP BY driver_id
    )

SELECT 
    f1.driver_id, 
    d.driver_name, 
    ROUND(f1.first_half_avg, 2) AS first_half_avg, 
    ROUND(f2.second_half_avg, 2) AS second_half_avg,
    ROUND(f2.second_half_avg - f1.first_half_avg, 2) AS efficiency_improvement
FROM FuelEarly f1
JOIN FuelLate f2 ON f1.driver_id = f2.driver_id
JOIN Drivers d ON f1.driver_id = d.driver_id
WHERE f2.second_half_avg - f1.first_half_avg > 0
ORDER BY f2.second_half_avg - f1.first_half_avg DESC