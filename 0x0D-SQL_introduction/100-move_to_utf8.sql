-- Script to convert the database hbtn_0c_0, table first_table, and field name to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Select the database
USE hbtn_0c_0;

-- Convert the table first_table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field name in first_table to utf8mb4
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
