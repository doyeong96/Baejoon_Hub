-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 
-- 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 보호 시작일 순으로 조회해야 합니다.

-- 둘을 조인해서 안나간애들은 null 값이 나올테고
-- 널 값인 애들중에서 오래된애들 순으로 정렬
-- 인 테이블 기준으로 레프트 조인하면 아웃 테이블 에서 널값 나오는애들이 아직 안나간애들
SELECT A.NAME, A.DATETIME FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3