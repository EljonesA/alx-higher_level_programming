-- Script to create table named first_table in current db if doesn't exist
-- with 2 columns id(int) & name(varchar 256)
-- SELECT/SHOW statements not allowed
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
