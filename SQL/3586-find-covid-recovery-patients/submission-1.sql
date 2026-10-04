# Write your MySQL query statement below
WITH Matched AS (
    SELECT
        c1.patient_id,
        DATEDIFF(MIN(c2.test_date), MIN(c1.test_date)) AS recovery_time
    FROM Covid_tests c1
    JOIN Covid_tests c2 ON c1.patient_id = c2.patient_id
                        AND c1.test_date < c2.test_date
                        AND c1.result = 'Positive'
                        AND c2.result = 'Negative'
    GROUP BY patient_id
)

SELECT m.patient_id, p.patient_name, p.age, m.recovery_time
FROM Matched m 
LEFT JOIN Patients p ON m.patient_id = p.patient_id
ORDER BY m.recovery_time ASC, p.patient_name ASC