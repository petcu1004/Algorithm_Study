-- 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기

SELECT A.CAR_ID, A.CAR_TYPE, FLOOR(A.DAILY_FEE*((100-B.DISCOUNT_RATE)/100)*30) AS FEE FROM CAR_RENTAL_COMPANY_CAR A
RIGHT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN B ON A.CAR_TYPE = B.CAR_TYPE
WHERE A.CAR_TYPE IN ('세단', 'SUV') AND B.duration_type = '30일 이상' AND A.DAILY_FEE*((100-B.DISCOUNT_RATE)/100)*30>=500000 AND A.DAILY_FEE*((100-B.DISCOUNT_RATE)/100)*30<2000000
AND A.CAR_ID NOT IN (
    SELECT CAR_ID FROM (
        SELECT C.CAR_ID FROM CAR_RENTAL_COMPANY_CAR C
            RIGHT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY D ON C.CAR_ID = D.CAR_ID
        WHERE (D.START_DATE <"2022-12-01" AND D.END_DATE>="2022-11-01")
    ) E 
)
ORDER BY FEE DESC, A.CAR_TYPE ASC ,A.CAR_ID DESC