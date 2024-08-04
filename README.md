# 0x0D. SQL - Introduction

This project is part of the ALX Higher Level Programming curriculum. It introduces the basics of SQL (Structured Query Language) and MySQL, a popular relational database management system.

## Learning Objectives

- Understand what a database is and how it is structured.
- Learn the basic SQL syntax and commands to interact with a database.
- Create and manage databases and tables using SQL.
- Perform CRUD (Create, Read, Update, Delete) operations on database records.
- Use aggregate functions and grouping to perform complex queries.

## Project Files

The following are the SQL scripts included in this project:

1. `0-list_databases.sql`: Lists all databases on the MySQL server.
2. `1-create_database_if_missing.sql`: Creates a database if it doesn't exist.
3. `2-remove_database.sql`: Removes a database if it exists.
4. `3-list_tables.sql`: Lists all tables in a database.
5. `4-first_table.sql`: Creates a table called `first_table`.
6. `5-full_table.sql`: Inserts records into `first_table`.
7. `6-list_values.sql`: Lists all records in `first_table`.
8. `7-insert_value.sql`: Inserts a new record into `first_table`.
9. `8-count_89.sql`: Counts the number of records with `id = 89` in `first_table`.
10. `9-full_creation.sql`: Creates a database and table, then inserts records.
11. `10-top_score.sql`: Retrieves the record with the highest score.
12. `11-best_score.sql`: Retrieves the highest score.
13. `12-no_cheating.sql`: Retrieves scores, excluding a specific name.
14. `13-change_class.sql`: Updates a record in `first_table`.
15. `14-average.sql`: Calculates the average score.
16. `15-groups.sql`: Groups records by a specific field.
17. `16-no_link.sql`: Retrieves records with NULL values in a specific field.
18. `100-move_to_utf8.sql`: Converts the database, table, and field to UTF8.
19. `101-avg_temperatures.sql`: Displays the average temperature by city, ordered by temperature.

## Usage

To run these SQL scripts, use the following command structure:

```sh
$ cat filename.sql | mysql -hlocalhost -uroot -p

Author
Sohil Hamdy - Sohilahamdy
License
This project is licensed under the MIT License - see the LICENSE file for details.
