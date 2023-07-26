-- Lists all records of the table 'second_table'
-- of the database hbtn_0c_0 in MySQL server
-- in descending order.
-- Doesn't list rows without a 'name' value.
-- Display 'score' and 'name' in this order.
-- The database name is passed as an argument to
-- the 'mysql' command.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
