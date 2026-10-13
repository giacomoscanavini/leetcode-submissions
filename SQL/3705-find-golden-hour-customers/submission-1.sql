# Write your MySQL query statement below
WITH CustomerAnalysis AS (
    SELECT 
        customer_id,
        SUM(IF(
            HOUR(order_timestamp) BETWEEN 11 AND 13 
            OR HOUR(order_timestamp) BETWEEN 18 AND 20, 
            1, 0)) AS num_peak_hour_orders,
        SUM(IF(
            order_rating IS NOT NULL, 
            1, 0)) AS num_rated_orders,
        COUNT(customer_id) AS total_orders,
        ROUND(AVG(order_rating), 2) AS average_rating
    FROM Restaurant_orders
    GROUP BY customer_id
)

SELECT 
    customer_id, 
    total_orders, 
    ROUND(100 * num_peak_hour_orders / total_orders) AS peak_hour_percentage,
    average_rating
FROM CustomerAnalysis
WHERE 
    total_orders >= 3
    AND num_peak_hour_orders / total_orders >= 0.6 
    AND average_rating >= 4.0
    AND num_rated_orders / total_orders >= 0.5
ORDER BY average_rating DESC, customer_id DESC