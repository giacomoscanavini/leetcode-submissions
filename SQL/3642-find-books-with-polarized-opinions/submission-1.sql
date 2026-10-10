# Write your MySQL query statement below
WITH 
    ValidBooks AS (
        SELECT 
            book_id,
            MAX(session_rating) - MIN(session_rating) AS rating_spread,
            ROUND(SUM(IF(session_rating <> 3, 1, 0)) / COUNT(*), 2) AS polarization_score 
        FROM Reading_sessions
        GROUP BY book_id
        HAVING 
            COUNT(*) >= 5
            AND MIN(session_rating) <= 2
            AND MAX(session_rating) >= 4
    )

SELECT 
    v.book_id, 
    b.title, b.author, b.genre, b.pages,
    v.rating_spread, v.polarization_score
FROM ValidBooks v
LEFT JOIN Books b ON v.book_id = b.book_id
WHERE v.polarization_score >= 0.6
ORDER BY v.polarization_score DESC, b.title DESC