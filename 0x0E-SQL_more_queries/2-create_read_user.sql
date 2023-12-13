-- point 2
-- create database user only select privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost;
GRANT USAGE ON *.* TO user_0d_2@localhost;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';
