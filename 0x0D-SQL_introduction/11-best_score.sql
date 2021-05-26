-- Display formatted results from a list
-- return table records ordered by score and include name:
SELECT score, name FROM second_table
WHERE score > 9 
ORDER BY score DESC;
