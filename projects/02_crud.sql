INSERT INTO movies
VALUES (20182530, '극한직업', '15세이상관람가', '이병현', 20190123, 3138467, 111, '한국', '코미디');

-- 입력한 영화의 정보가 입력되었는지 확인
SELECT * FROM movies WHERE 영화코드 = 20182530;

-- 과거 데이터 출력 후, 삭제
SELECT * FROM movies WHERE 영화코드 = 20040521;
DELETE FROM movies WHERE 영화코드 = 20040521;

-- 영화코드 20185124 데이터 출력 후, data 수정
SELECT * FROM movies WHERE 영화코드 = 20185124;
UPDATE movies SET 감독="없음" WHERE 영화코드 = 20185124;