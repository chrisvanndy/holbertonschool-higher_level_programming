-- Create table id_not_null 
-- if id_not_null exists script will not fail
CREATE TABLE `id_not_null` (
	`id` INT SET DEFAULT 1,
	`name` VARCHAR(256)
);
