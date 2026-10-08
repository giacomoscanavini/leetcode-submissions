# Write your MySQL query statement below
WITH 
    Ranked AS (
        SELECT 
            store_id, 
            product_name, 
            quantity, 
            price, 
            ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price DESC) AS most_exp,
            ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price ASC) AS most_cheap
        FROM Inventory
        WHERE store_id IN (
            SELECT store_id
            FROM Inventory
            GROUP BY store_id
            HAVING COUNT(DISTINCT product_name) >= 3
        )
    ), 
    Expensive AS (
        SELECT store_id, product_name, quantity 
        FROM Ranked 
        WHERE most_exp = 1
    ),
    Cheap AS (
        SELECT store_id, product_name, quantity 
        FROM Ranked 
        WHERE most_cheap = 1
    )

SELECT
    e.store_id, 
    s.store_name, 
    s.location,
    e.product_name AS most_exp_product,
    c.product_name AS cheapest_product,
    ROUND(c.quantity / e.quantity, 2) AS imbalance_ratio
FROM Expensive e
JOIN Cheap c ON e.store_id = c.store_id 
JOIN Stores s ON e.store_id = s.store_id
WHERE c.quantity > e.quantity
ORDER BY ROUND(c.quantity / e.quantity, 2) DESC, s.store_name ASC