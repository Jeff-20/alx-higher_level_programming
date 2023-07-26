-- computes the score average of all the records
-- in the table 'second_table' of the database
-- 'htbn_0c_0' in MySQL server.
-- The database name is passed as an argument
-- of the 'mysql' command.
SELECT AVG(score) AS average
FROM second_table;
