SELECT MAX(num) as num
FROM (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1) AS a

SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
);