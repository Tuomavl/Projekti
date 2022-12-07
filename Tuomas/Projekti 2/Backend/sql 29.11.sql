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
    airportName VARCHAR(50),
    cityName VARCHAR(50),
    welcomeText VARCHAR(500),
    suspectName VARCHAR(50)
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
    story VARCHAR(1000) NOT NULL UNIQUE
);


INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (1,'Puola','Warsaw Chopin Airport','Varsova');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (2,'Unkari','Budapest Liszt Ferenc International Airport','Budapest');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (3,'Kroatia','Zagreb Airport','Zagreb');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (4,'Itävalta','Vienna International Airport','Wien');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (5,'Tsekki','Václav Havel Airport Prague','Praha');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (6,'Saksa','Berlin Brandenburg Airport','Berliini');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (7,'Tanska','Copenhagen Kastrup Airport','Kööpenhamina');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (8,'Alankomaat','Amsterdam Airport Schiphol','Amsterdam');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (9,'Italia','Leonardo da Vinci–Fiumicino Airport','Rooma');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (10,'Ranska','Paris-Orly Airport','Pariisi');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (11,'Ruotsi','Stockholm-Arlanda Airport','Tukholma');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (12,'Kreikka','Athens Eleftherios Venizelos Internation','Ateena');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (13,'Albania','Tirana International Airport Mother Tere','Tirana');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (14,'Romania','Henri Coanda International Airport','Bukarest');

INSERT INTO gameCountries (countryID, name, airportName,cityName)
VALUES (15,'Iso-Britannia','London City Airport','Lontoo');



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

INSERT INTO suspects (name,status,story)
VALUES ('Mary',0,'Mary: He-he-hei ri-rikos-rikostutkija {playerName}. A-ai tu-tulit haas-haastattelemaan mi-mi-minua. \nA-ai mi-mi-mi-miksi pa-pakenin? No tuo-tuota mi-minä va-vain pe-peläs-tyin. Mu-mutta se en o-le oikeasti minä! Mi-minä lupaan! \nUskoi-sit mi-minua! Mu-mutta näi-in, että {addSuspect} me-meni lounaalle, joten en usko, että hän on murhaaja. Kiva, jos pystyin olla avuksi!');

INSERT INTO suspects (name,status,story)
VALUES('Luke',0,'Luke: Minulla olisi tässä nyt kiire en millään ehtisi... jaahas epäillään murhasta vai? No en se minä ollut. \nEnkä tiedä kuka se oli. Voisinko nyt mennä? Ei minulla ole mitään kerrottavaa! \nPaitsi että... no tuota näin, kun {addSuspect} lähti aikaisemmalla lennolla, joten se on tuskin hän. Nyt minun on kuitenkin pakko mennä näkemiin.');

INSERT INTO suspects (name,status,story)
VALUES('Sandra',0,'Sandra: Ai hei rikostutkija... {playerName}. Teilläpä on ihana nimi. Ai tulitte haastattelemaan minua. Sepä kovin mukavaa. \nJatkettaisiinko haastattelua jossain mukavammassa paikassa. Ai sinulla on kiire? \nNo kyllä me kerkeäisimme nope- selvä selvä pysytään asiassa, vaikka se onkin vaikeaa, kun katselee noita silmiäsi. \nNäinkö jotain epäilyttävää? En. En sitten mitään. Toki, jos haluaisit jatkaa juttelemista minun hotellillani- \nAi jaaha selvä no {addSuspect} se ei ole, koska hän oli toisessa palaverissa tapahtumien aikaan. Eikö rikostutkijalla olisi edes pieni hetki aikaa- aha no heippa sitten. Nähdään taas pian!');

INSERT INTO suspects (name,status,story)
VALUES('Tom',0,'Tom: No terve. Tietenkään minä en ole murhaaja eikä ole myöskään {addSuspect}. \nAi mistä tiedän? Koska tiedän vain. Häivyhän siitä sitten jo.');

INSERT INTO suspects (name,status,story)
VALUES('Adam',0,'Adam: Terveppä terve! Murhatutkimuksen tiimoilta tullut minua tapaamaan? Hahah. Naurettava ajatus, että minua edes epäillään. \nMutta kuulepas tätä. Näin, että {addSuspect} hiippaili hotellihuoneeseen jonkun tuntemattoman kanssa! \nMehukas juoru, mutta samalla taitaa todistaa, ettei hän voi olla murhaaja.');

INSERT INTO suspects (name,status,story)
VALUES('Stefan',0,'Stefan: Terve {playername}! Mennään suoraan asiaan. Juuri ennen tapahtunutta {addSuspect} \nlähti hakemaan kaikille kahvia ja palasi vasta myöhemmin. Hänellä on siis vahva alibi, kahvilan työntekijät voivat varmasti taata sen. \nJatkahan sitten tutkimuksiasi ja minä pääsen jatkamaan töitäni, hyvästi!');

INSERT INTO suspects (name,status,story)
VALUES('Kristen',0,'Kristen: Moi. Aivan, kuulinkin huhuja tästä. En kyllä yhtään yllättynyt, tunnelma (konferenssissa tai missä ny olivatkaa) oli hyvin jännittynyt. \n{addSuspect} oli kylläkin kokoajan näköetäisyydelläni, joten hän se ei ole. Kerrothan kun kuulet lisää, heippa!');

INSERT INTO suspects (name,status,story)
VALUES('Jake',0,'Jake: Hauska tavata! Murha?? Ei kai… Kuinka kamalaa! Olen aivan järkyttynyt… Mitäkö tiedän siitä?\n En.. en mitään, en voi edes ajatella, olen niin kauhuissani. Ajatella, että olen saattanut keskustella murhaajan kanssa!\n Ei, en pysty käsittelemään tätä, en kykene nyt vastaamaan kysymyksiin. {addSuspect} oli tauolla käymässä ulkona, joten hänellä ei ollut tuohon hirmutekoon mahdollisuutta.\n Huh.. Minun pitää nyt päästä pitkälleni, hei hei!');
