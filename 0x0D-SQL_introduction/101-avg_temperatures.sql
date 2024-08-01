-- Replace 'your_table_name' with the actual name of your table
-- Assuming the table has columns 'city' and 'temperature'
SELECT
    city,
    ROUND(AVG(temp), 4) AS avg_temp
FROM
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp DESC;
