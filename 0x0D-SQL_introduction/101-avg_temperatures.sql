-- Script to display average temperature by city, ordered by temperature (descending)

-- Assuming the table name is temperatures and it has columns: city and temperature
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
