SELECT player_id, event_date AS first_login
FROM activity a
GROUP BY player_id
HAVING MIN(event_date)