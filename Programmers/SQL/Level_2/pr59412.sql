-- 59412. 입양 시각 구하기(1)

SELECT DATE_FORMAT(DATETIME, '%H') AS HOUR, COUNT(*) AS COUNT 
    FROM ANIMAL_OUTS 
    GROUP BY HOUR 
    HAVING HOUR BETWEEN 9 AND 19 
    ORDER BY HOUR;
  