-- Creates database and user for testing
CREATE DATABASE IF NOT EXISTS `test_db` 
CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'test_password';
GRANT ALL PRIVILEGES ON test_db.* TO 'test_user'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'test_user'@'localhost';
FLUSH PRIVILEGES;