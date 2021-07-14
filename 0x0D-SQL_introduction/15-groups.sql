-- Lists the number of records with the same score
-- in the "second_table" from "hbtn_0c_0"
SELECT score, COUNT(*) AS number
		FROM second_table
		GROUP BY score
		ORDER BY score DESC;
