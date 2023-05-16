-- script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server.
SELECT *
FROM information_schema.columns
WHERE table_name = "first_table";
