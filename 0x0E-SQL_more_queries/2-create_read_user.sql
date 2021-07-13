-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- script
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'newuser'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = PASSWORD('user_0d_2_pwd');
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
