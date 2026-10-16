# Write your MySQL query statement below
WITH 
    ByCategory AS (
        SELECT 
            p.user_id, i.category
        FROM ProductPurchases p
        LEFT JOIN ProductInfo i ON p.product_id = i.product_id
    ),
    Crossed AS (
        SELECT DISTINCT 
            b1.user_id, 
            b1.category AS category1,
            b2.category AS category2
        FROM ByCategory b1
        CROSS JOIN ByCategory b2
        WHERE 
            b1.user_id = b2.user_id 
            AND b1.category < b2.category
    )

SELECT category1, category2, COUNT(user_id) AS customer_count
FROM Crossed 
GROUP BY category1, category2
HAVING COUNT(user_id) >= 3
ORDER BY customer_count DESC, category1 ASC, category2 ASC