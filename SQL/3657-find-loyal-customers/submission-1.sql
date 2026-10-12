# Write your MySQL query statement below
WITH CustomerAnalysis AS (
    SELECT 
        customer_id,
        DATEDIFF(MAX(transaction_date), MIN(transaction_date)) AS activity_period,
        SUM(IF(transaction_type = 'refund', 1, 0)) AS refunded,
        COUNT(*) AS total
    FROM Customer_transactions 
    GROUP BY customer_id
)

SELECT customer_id
FROM CustomerAnalysis
WHERE 
    activity_period >= 30 
    AND total - refunded >= 3
    AND refunded / total < 0.2
ORDER BY customer_id ASC
