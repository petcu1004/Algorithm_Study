-- 오프라인/온라인 판매 데이터 통합하기

SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d"), PRODUCT_ID, USER_ID, SALES_AMOUNT FROM ONLINE_SALE 
WHERE SALES_DATE LIKE "2022-03%"
UNION ALL
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d"), PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT FROM OFFLINE_SALE  
WHERE SALES_DATE LIKE "2022-03%"
ORDER BY 1, 2, 3