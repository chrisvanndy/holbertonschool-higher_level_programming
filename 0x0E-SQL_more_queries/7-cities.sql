-- create database hbtn_0d_usa
-- create table cities in ^^ database
-- id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
-- FOREIGN KEY state_id references states table
-- name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256),
	FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
