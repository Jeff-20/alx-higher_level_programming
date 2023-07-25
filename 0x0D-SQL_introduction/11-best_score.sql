-- Lists all the records of 'name' and 'score'
-- of the table 'second_table' in this order,
-- with a score >= 10,
-- of the database 'htbn_0c_0' in MySQL server.
-- The records are ordered by 'score' in descending
-- order.
SELECT score, name FROM second_table
WHERE score>=10
ORDER BY score DESC;
