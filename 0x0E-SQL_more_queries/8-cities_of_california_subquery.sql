-- list all cities of California found in database
-- states contains id and name(state)
-- format restuls; SELECT id, name (from cities)
-- format results: id ascending
SELECT `id`, `name`FROM `cities`
WHERE `state_id` IN
	(SELECT `id` FROM `states` WHERE `name` = "California")
ORDER BY `id`;
