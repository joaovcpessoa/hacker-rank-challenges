-- Query the two cities in STATION with the shortest and longest CITY names, 
-- as well as their respective lengths (i.e.: number of characters in the name).
-- If there is more than one smallest or largest city, choose the one that comes 
-- first when ordered alphabetically.
SELECT 
    CITY, 
    LENGTH(CITY) AS CITY_LENGTH
FROM 
    STATION
ORDER BY LENGTH(CITY), CITY
FETCH FIRST ROW ONLY;

SELECT 
    CITY,
    LENGTH(CITY) AS CITY_LENGTH
FROM 
    STATION
ORDER BY LENGTH(CITY) DESC, CITY
FETCH FIRST ROW ONLY;