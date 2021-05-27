-- write script that lists all cities contained in the database
-- output format: cities.id - cities.name - states.name
-- output format: ascending cities.id
-- ONLY ONE SELECT STATEMETN
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
-- cities.state_id = state.id
-- format wants to print cities.name so INNER JOIN sates + common elements
	FROM `cities` INNER JOIN `states` ON `cities`.`state_id` = `state`.`id`
ORDER BY `cities`.`id`;
