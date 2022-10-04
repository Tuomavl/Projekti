CREATE USER 'lentopeli'@'localhost' IDENTIFIED BY 'peli';

GRANT ALL PRIVILEGES ON flight_game.* TO 'lentopeli'@'localhost';

DROP TABLE IF EXISTS `players`;

USE flight_game;

CREATE TABLE players(
    playerID INTEGER NOT NULL PRIMARY KEY,
    playerName VARCHAR(20) NOT NULL UNIQUE,
    wins INTEGER,
    losses INTEGER,
    amountPlayed INTEGER,
    winStreak INTEGER
);
