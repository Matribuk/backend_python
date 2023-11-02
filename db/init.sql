CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL
);

INSERT INTO tasks (task) VALUES
    ('Buy Coffee'),
    ('Go eat salt'),
    ('Be smooth operator');

INSERT INTO user (username) VALUES ('user1');
INSERT INTO user (username) VALUES ('user2');


