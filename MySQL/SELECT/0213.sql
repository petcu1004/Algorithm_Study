-- 평균 일일 대여 요금 구하기

SELECT ROUND(avg(daily_fee),0) AS AVERAGE_FEE from CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE = 'SUV'