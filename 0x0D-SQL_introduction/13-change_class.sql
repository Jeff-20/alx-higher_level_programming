-- removes all records with a score <= 5 in the
-- table 'second_table' of the database 'htbn_0c_0'
-- in MySQL server.
-- The database name is passed as an argument of the
-- 'mysql' command
DELETE FROM second_table
WHERE score <= 5;