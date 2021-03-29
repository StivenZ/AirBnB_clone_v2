-- Creates database and user
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE DATABASE IF NOT EXISTS `performance_schema`;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE `hbnb_dev_db`;
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE `performance_schema`;
GRANT SELECT ON `performance_schema`.* to 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
