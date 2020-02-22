1. Extract city data for Barcelona, Spain from the database and save it to CSV
SELECT year, avg_temp
FROM city_data
WHERE city='Barcelona' AND country='Spain'

2. Extract global data and save it to CSV
SELECT *
FROM global_data
