-- Lists all records of the "second_table" from "hbtn_0c_0"
-- listing the rows with "name" value
SELECT score, name FROM second_table
		WHERE name IS NOT NULL
		ORDER BY score DESC;
