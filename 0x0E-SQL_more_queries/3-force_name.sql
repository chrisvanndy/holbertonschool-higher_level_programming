-- Create a table named force_name with id INT, name VC(256) NOT NULL
-- if the table already exists the script should not fail
CREATE TABLE IF NOT EXISTS `force_name`(
	`id` INT, 
	`name` VARCHAR(256) NOT NULL
); 
