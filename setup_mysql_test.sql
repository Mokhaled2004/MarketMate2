-- Prepares a MySQL Test server for the project.

CREATE DATABASE IF NOT EXISTS marketmate_test_db;
CREATE USER IF NOT EXISTS 'marketmate_test'@'localhost' IDENTIFIED BY 'marketmate_test_pwd';
GRANT ALL PRIVILEGES ON marketmate_test_db . * TO 'marketmate_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'marketmate_test'@'localhost';
