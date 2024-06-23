-- Prepares a MySQL server for the project.

CREATE DATABASE IF NOT EXISTS marketmate_dev_db;
CREATE USER IF NOT EXISTS 'marketmate_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON marketmate_dev_db . * TO 'marketmate_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'marketmate_dev'@'localhost';
