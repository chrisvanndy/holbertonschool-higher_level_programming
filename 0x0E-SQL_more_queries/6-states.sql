-- create a database hbtn_0d_usa
-- create table states in ^^^ database
-- id is INT auto_generated not null and a primary key(unique)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256)
);
