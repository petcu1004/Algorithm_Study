-- 헤비 유저가 소유한 장소 - Level 3

-- 오랜만에 작성하니 감을 잡느라 시간이 좀 걸림.. 하지만 코드 참고 없이 스스로 풀어냄!

-- 헤비 유저를 가져오기 위해 먼저 SELECT HOST_ID, COUNT(HOST_ID) FROM PLACES GROUP BY HOST_ID HAVING COUNT(HOST_ID)>1 를 작성하고 이를 내부 쿼리문에 집어넣음

-- 정답은 아래 코드와 같음
SELECT * FROM PLACES 
WHERE HOST_ID IN 
    (SELECT HOST_ID FROM 
     (SELECT HOST_ID, COUNT(HOST_ID) FROM PLACES 
      GROUP BY HOST_ID HAVING COUNT(HOST_ID)>1) E
    )
ORDER BY ID

-- 내부 쿼리문에서 HOST_ID는 안가져오고, COUNT(HOST_ID)만 넣어서 계속 틀렸음..
-- 그리고, WHERE COUNT(HOST_ID)>1문으로 쓰려고 해서 틀렸음.
-- 그룹화로 적용된 테이블에서 HAVING으로 조건을 주었어야 했음!!
-- 내부 쿼리문을 따로 빼서 작성해보니 문제를 쉽게 찾을 수 있었음.
-- SELECT HOST_ID, COUNT(HOST_ID) FROM PLACES WHERE HOST_ID>1 GROUP BY HOST_ID 이렇게 작성했다면 HOST_ID는 INT이기 때문에 단순하게 1이상인 ID 값을 가져오게 해서 모든 아이디를 가져오게 되는 것을 확인 후 HAVING절로 변경함

-- 쉽게 보이지만 사실 그리 쉽지 않음 문제라고 판단됨.