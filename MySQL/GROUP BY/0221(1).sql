-- 입양 시각 구하기(1)

SELECT DATE_FORMAT(DATETIME, '%H') AS HOUR, COUNT(DATE_FORMAT(DATETIME, '%h')) AS COUNT FROM ANIMAL_OUTS 
GROUP BY HOUR
HAVING HOUR>=9 AND HOUR <20
ORDER BY HOUR