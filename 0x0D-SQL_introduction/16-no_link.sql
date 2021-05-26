-- script lists all records of table where name is not null
-- results should be formated score desc followed by name colum
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
