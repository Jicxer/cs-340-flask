DROP TABLE IF EXISTS members;

CREATE TABLE `members` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `dob` DATE NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    CONSTRAINT full_name UNIQUE (first_name,last_name)
);

DROP TABLE IF EXISTS clubs;

CREATE TABLE `clubs` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `phonenumber` varchar(15) NOT NULL
);

DROP TABLE IF EXISTS 'events';

CREATE TABLE `events` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE NOT NULL,
    `public_or_private` BIT
);

DROP TABLE IF EXISTS sponsors;


CREATE TABLE `sponsors` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    `service_id` INTEGER AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `phonenumber` varchar(15) NOT NULL
);



