-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
-- Your result cannot contain duplicates.
SELECT DISTINCT
    CITY
FROM 
    STATION
WHERE
    CASE
        WHEN UPPER(SUBSTR(CITY, 1, 1)) IN ('A', 'E', 'I', 'O', 'U') THEN 1
        ELSE 0
    END = 1;