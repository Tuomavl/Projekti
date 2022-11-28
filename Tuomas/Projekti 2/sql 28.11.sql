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
    winStreak INTEGER,
    Highest_Win_Streak integer
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

DROP TABLE IF EXISTS `suspects`;

CREATE TABLE suspects(
    name VARCHAR(50) NOT NULL UNIQUE,
    status INTEGER,
    story VARCHAR(500) NOT NULL UNIQUE
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
VALUES (7,'Tanska','Copenhagen Kastrup Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (8,'Alankomaat','Amsterdam Airport Schiphol');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (9,'Italia','Leonardo da Vinci–Fiumicino Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (10,'Ranska','Paris-Orly Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (11,'Ruotsi','Stockholm-Arlanda Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (12,'Kreikka','Athens Eleftherios Venizelos Internation');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (13,'Albania','Tirana International Airport Mother Tere');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (14,'Romania','Henri Coanda International Airport');

INSERT INTO gameCountries (countryID, name, airportName)
VALUES (15,'Iso-Britannia','London City Airport');



INSERT INTO flights (countryID, joinID)
VALUES (1,2),(1,5),(1,7),(1,11);

INSERT INTO flights (countryID, joinID)
VALUES (2,1),(2,4),(2,14);

INSERT INTO flights (countryID, joinID)
VALUES (3,4),(3,9);

INSERT INTO flights (countryID, joinID)
VALUES (4,2),(4,3),(4,5),(4,6);

INSERT INTO flights (countryID, joinID)
VALUES (5,1),(5,4),(5,6),(5,7);

INSERT INTO flights (countryID, joinID)
VALUES (6,4),(6,5),(6,8),(6,9);

INSERT INTO flights (countryID, joinID)
VALUES (7,1),(7,5),(7,8),(7,11);

INSERT INTO flights (countryID, joinID)
VALUES (8,6),(8,7),(8,10);

INSERT INTO flights (countryID, joinID)
VALUES (9,4),(9,6),(9,10),(9,13);

INSERT INTO flights (countryID, joinID)
VALUES (10,8),(10,9);

INSERT INTO flights (countryID, joinID)
VALUES (11,1),(11,7);

INSERT INTO flights (countryID, joinID)
VALUES (12,14),(12,13);

INSERT INTO flights (countryID, joinID)
VALUES (13,12),(13,9),(13,14);

INSERT INTO flights (countryID, joinID)
VALUES (14,2),(14,12),(14,13);

INSERT INTO flights (countryID, joinID)
VALUES (15,8),(15,10);

INSERT INTO suspects (name,status,story);
VALUES ('Mary',0,'Mary: He-he-hei ri-rikos-rikostutkija {playerName}. A-ai tu-tulit haas-haastattelemaan mi-mi-minua. \nA-ai mi-mi-mi-miksi pa-pakenin? No tuo-tuota mi-minä va-vain pe-peläs-tyin. Mu-mutta se en o-le oikeasti minä! Mi-minä lupaan! \nUskoi-sit mi-minua! Mu-mutta näi-in, että Mary me-meni vessaan, joten en usko, että hän on murhaaja. Kiva, jos pystyin olla avuksi!');

INSERT INTO suspects (name,status,story);
VALUES('Luke',0,'Luke: Minulla olisi tässä nyt kiire en millään ehtisi... jaahas epäillään murhasta vai? No en se minä ollut. \nEnkä tiedä kuka se oli. Voisinko nyt mennä? Ei minulla ole mitään kerrottavaa! \nPaitsi että... no tuota näin, kun {person_dictionary["Luke"]} lähti aikaisemmalla lennolla, joten se on tuskin hän. Nyt minun on kuitenkin pakko mennä näkemiin.');

INSERT INTO suspects (name,status,story);
VALUES('Sandra',0,'Sandra: Ai hei rikostutkija... {playerName}. Teilläpä on ihana nimi. Ai tulitte haastattelemaan minua. Sepä kovin mukavaa. \nJatkettaisiinko haastattelua jossain mukavammassa paikassa. Ai sinulla on kiire? \nNo kyllä me kerkeäisimme nope- selvä selvä pysytään asiassa, vaikka se onkin vaikeaa, kun katselee noita silmiäsi. \nNäinkö jotain epäilyttävää? En. En sitten mitään. Toki, jos haluaisit jatkaa juttelemista minun hotellillani- \nAi jaaha selvä no {person_dictionary["Sandra"]} se ei ole, koska minä olin hänen kanssaan. Eikö rikostutkijalla olisi edes pieni hetki aikaa- aha no heippa sitten. Nähdään taas pian!');

INSERT INTO suspects (name,status,story);
VALUES('Tom',0,'Tom: No terve. Tietenkään minä en ole murhaaja eikä ole myöskään {person_dictionary["Tom"]}. \nAi mistä tiedän? Koska tiedän vain. Häivyhän siitä sitten jo.');

INSERT INTO suspects (name,status,story);
VALUES('Adam',0,'Adam: Terveppä terve! Murhatutkimuksen tiimoilta tullut minua tapaamaan? Hahah. Naurettava ajatus, että minua edes epäillään. \nMutta kuulepas tätä. Näin, että {person_dictionary["Adam"]} hiippaili hotellihuoneeseen jonkun tuntemattoman kanssa! \nMehukas juoru, mutta samalla taitaa todistaa, ettei hän voi olla murhaaja.');

INSERT INTO suspects (name,status,story);
VALUES('Stefan',0,);

INSERT INTO suspects (name,status,story);
VALUES('Kristen',0,);

INSERT INTO suspects (name,status,story);
VALUES('Jake',0,);
