-- Updates the score of Bob to 10 in the table 'second_table'
-- using only the 'name' field.
-- The database name is passed as an argument of the 'mysql'
-- command.
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
