-- 상품 별 오프라인 매출 구하기

SELECT A.PRODUCT_CODE, (A.PRICE*SUM(B.SALES_AMOUNT)) AS SALES FROM PRODUCT A
RIGHT JOIN OFFLINE_SALE B ON A.PRODUCT_ID = B.PRODUCT_ID
GROUP BY A.PRODUCT_ID
ORDER BY 2 DESC, 1 ASC