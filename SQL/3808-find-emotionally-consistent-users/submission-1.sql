# Write your MySQL query statement below
WITH 
    ReactionsPerUser AS (
        SELECT 
            user_id,
            COUNT(content_id) AS nReactions
        FROM Reactions
        GROUP BY user_id
        HAVING COUNT(content_id) >= 5
    ),
    ReactionAnalysis AS (
        SELECT 
            user_id,
            reaction,
            COUNT(reaction) AS count_per_reaction
        FROM Reactions
        GROUP BY user_id, reaction
    ),
    Ranked AS (
        SELECT
            user_id,
            reaction,
            count_per_reaction,
            ROW_NUMBER() OVER (
                PARTITION BY user_id, reaction
                ORDER BY count_per_reaction DESC
            ) AS ranked
        FROM ReactionAnalysis
    )

SELECT 
    r.user_id, 
    r.reaction AS dominant_reaction,
    ROUND(r.count_per_reaction / u.nReactions, 2) AS reaction_ratio
FROM Ranked r
JOIN ReactionsPerUser u ON r.user_id = u.user_id 
WHERE 
    r.ranked = 1
    AND r.count_per_reaction / u.nReactions >= 0.6
ORDER BY reaction_ratio DESC, r.user_id ASC