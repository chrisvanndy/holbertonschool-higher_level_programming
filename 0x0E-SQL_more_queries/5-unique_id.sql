-- Create the table unique_id 
-- id value must be set to defatul 1 and must be unique
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
