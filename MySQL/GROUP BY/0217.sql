-- 진료과별 총 예약 횟수 출력하기WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
# HAVING COUNT(MCDP_CD)
ORDER BY COUNT(MCDP_CD) ASC, MCDP_CD ASC