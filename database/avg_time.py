SELECT mashine_id, ROUND(
    AVG(CASE WHEN activity_type = 'end' THEN timestamp) -
    AVG(CASE WHEN activity_type='start' THEN timestamp),
3) AS processing_time
FROM Activity
GROUP BY mashine_id
