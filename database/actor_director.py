SELECT actor_id, director_id
  FROM Actordirector
  GROUP BY actor_id
  HAVING COUNT(timestamp) >= 3