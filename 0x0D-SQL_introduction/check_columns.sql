-- Script to list columns of the table first_table
SELECT COLUMN_NAME 
FROM information_schema.COLUMNS 
WHERE TABLE_NAME = 'first_table' 
  AND TABLE_SCHEMA = 'hbtn_0c_0';
