CREATE USER 'lentopeli'@'localhost' IDENTIFIED BY 'peli';

GRANT ALL PRIVILEGES ON flight_game.* TO 'lentopeli'@'localhost';

USE flight_game;


DROP TABLE IF EXISTS `players`;

CREATE TABLE players(
    playerID INTEGER NOT NULL PRIMARY KEY,
    playerName VARCHAR(20) NOT NULL UNIQUE,
    wins INTEGER,
    losses INTEGER,
    amountPlayed INTEGER,
    winStreak INTEGER
);

DROP TABLE IF EXISTS `gameCountries`;

CREATE TABLE gameCountries(
    countryID INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    airportName VARCHAR(50)
);

DROP TABLE IF EXISTS `flights`;

CREATE TABLE flights(
    countryID INTEGER NOT NULL,
    joinID INTEGER NOT NULL
);



INSERT INTO gameCountries (countryID, name, airportName)
VALUES (1,'Puola','Warsaw Chopin Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (2,'Unkari','Budapest Liszt Ferenc International Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (3,'Kroatia','Zagreb Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (4,'Itävalta','Vienna International Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (5,'Tsekki','Václav Havel Airport Prague');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (6,'Saksa','Berlin Brandenburg Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (7,'Tanska','Billund Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (8,'Alankomaat','Amsterdam Airport Schiphol');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (9,'Italia','Cagliari Elmas Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (10,'Ranska','Paris-Orly Airport');



INSERT INTO flights (countryID, joinID)
VALUES (1,2),(1,5),(1,7);

INSERT INTO flights (countryID, joinID)
VALUES (2,1),(2,4);

INSERT INTO flights (countryID, joinID)
VALUES (3,4),(3,9);

INSERT INTO flights (countryID, joinID)
VALUES (4,2),(4,3),(4,5),(4,6);

INSERT INTO flights (countryID, joinID)
VALUES (5,1),(5,4),(5,6),(5,7);

INSERT INTO flights (countryID, joinID)
VALUES (6,4),(6,5),(6,8),(6,9);

INSERT INTO flights (countryID, joinID)
VALUES (7,1),(7,5),(7,8);

INSERT INTO flights (countryID, joinID)
VALUES (8,6),(8,7),(8,10);

INSERT INTO flights (countryID, joinID)
VALUES (9,4),(9,6),(9,10);

INSERT INTO flights (countryID, joinID)
VALUES (10,8),(10,9);
