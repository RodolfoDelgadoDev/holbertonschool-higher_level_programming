-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
CREATE IF NOT EXIST USER 'user_0d_1'@'localhost';
SHOW GRANTS FOR user_0d_1@localhost;
SHOW GRANTS FOR user_0d_2@localhost;
