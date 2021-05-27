-- Create database hbtn_0d_2, if it doesn't exist
-- Create new user user_0d_2 with password user_0d_2_pwd, if not exists
-- GRANT SELETCT(read only) permissions to the specified user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
