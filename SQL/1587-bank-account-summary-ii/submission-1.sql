# Write your MySQL query statement below
WITH Balances AS (
    SELECT account, SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
    HAVING SUM(amount) > 10000
)

SELECT u.name, b.balance
FROM Balances b
LEFT JOIN Users u ON b.account = u.account 