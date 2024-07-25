-- Script to list all records from second_table with score >= 10, displaying score and name, ordered by score in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
