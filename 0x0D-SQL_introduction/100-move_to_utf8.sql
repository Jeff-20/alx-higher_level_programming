-- This script converts 'hbtn_0c_0' database 
-- (including table 'first_table', field 'name' in first_table)
-- to UTF8 in MySQL server.

-- Database hbtn_0c_0 to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- first_table to UTF8
-- USE hbtn_0c_0;
-- ALTER TABLE first_table
-- CONVERT TO CHARACTER SET utf8mb4
-- COLLATE utf8mb4_unicode_ci;
