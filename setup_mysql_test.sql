-- Sets up server for testing
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
USE `hbnb_test_db`;
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
USE `performance_schema`;
GRANT SELECT ON `performance_schema`.* to 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
