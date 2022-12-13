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
    lat INTEGER NOT NULL,
    lon INTEGER NOT NULL,
    airportName VARCHAR(50),
    cityName VARCHAR(50),
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


INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (1, 'Puola', 'Warsaw Chopin Airport', 'Varsova', 52.1656990051, 20.967100143399996);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (2, 'Unkari', 'Budapest Liszt Ferenc International Airport', 'Budapest', 47.42976, 19.261093);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (3, 'Kroatia', 'Zagreb Airport', 'Zagreb', 45.7429008484, 16.0687999725);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (4, 'Itävalta', 'Vienna International Airport', 'Wien', 48.110298, 16.568497726);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (5, 'Tsekki', 'Václav Havel Airport Prague', 'Praha', 50.1008, 14.26);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (6, 'Saksa', 'Berlin Brandenburg Airport', 'Berliini', 52.351389, 13.493889);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (7,'Tanska','Copenhagen Kastrup Airport','Kööpenhamina', 55.617900848389, 12.650462);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (8, 'Alankomaat', 'Amsterdam Airport Schiphol', 'Amsterdam', 52.308601, 4.76389);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (9, 'Italia', 'Leonardo da Vinci–Fiumicino Airport', 'Rooma', 41.804532, 12.251998);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (10, 'Ranska', 'Paris-Orly Airport', 'Pariisi', 48.7233333, 2.3794444);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (11, 'Ruotsi', 'Stockholm-Arlanda Airport', 'Tukholma', 59.651901245117, 17.918600082397);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (12, 'Kreikka', 'Athens Eleftherios Venizelos Internation', 'Ateena', 37.936401, 23.9445);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (13, 'Albania', 'Tirana International Airport Mother Tere', 'Tirana', 41.4146995544, 19.7206001282);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (14, 'Romania','Henri Coanda International Airport', 'Bukarest', 44.5711111, 26.085);

INSERT INTO gameCountries (countryID, name, airportName,cityName, lat, lon)
VALUES (15, 'Iso-Britannia', 'London City Airport', 'Lontoo', 51.505299, 0.055278);



INSERT INTO flights (countryID, joinID)
VALUES (1,6),(1,4),(1,11);

INSERT INTO flights (countryID, joinID)
VALUES (2,3),(2,4),(2,14);

INSERT INTO flights (countryID, joinID)
VALUES (3,4),(3,2),(3,14),(3,13);

INSERT INTO flights (countryID, joinID)
VALUES (4,2),(4,3),(4,5),(4,1),(4,9);

INSERT INTO flights (countryID, joinID)
VALUES (5,4),(5,6),(5,10);

INSERT INTO flights (countryID, joinID)
VALUES (6,7),(6,1),(6,5);

INSERT INTO flights (countryID, joinID)
VALUES (7,8),(7,11),(7,6);

INSERT INTO flights (countryID, joinID)
VALUES (8,7),(8,10),(8,15);

INSERT INTO flights (countryID, joinID)
VALUES (9,4),(9,10),(9,13);

INSERT INTO flights (countryID, joinID)
VALUES (10,8),(10,9),(10,15),(10,5);

INSERT INTO flights (countryID, joinID)
VALUES (11,1),(11,7);

INSERT INTO flights (countryID, joinID)
VALUES (12,14),(12,13);

INSERT INTO flights (countryID, joinID)
VALUES (13,3),(13,9),(13,12);

INSERT INTO flights (countryID, joinID)
VALUES (14,2),(14,12),(14,3);

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
VALUES('Stefan',0,'Stefan: Terve {playerName}! Mennään suoraan asiaan. Juuri ennen tapahtunutta {addSuspect} \nlähti hakemaan kaikille kahvia ja palasi vasta myöhemmin. Hänellä on siis vahva alibi, kahvilan työntekijät voivat varmasti taata sen. \nJatkahan sitten tutkimuksiasi ja minä pääsen jatkamaan töitäni, hyvästi!');

INSERT INTO suspects (name,status,story)
VALUES('Kristen',0,'Kristen: Moi. Aivan, kuulinkin huhuja tästä. En kyllä yhtään yllättynyt, tunnelma (konferenssissa tai missä ny olivatkaa) oli hyvin jännittynyt. \n{addSuspect} oli kylläkin kokoajan näköetäisyydelläni, joten hän se ei ole. Kerrothan kun kuulet lisää, heippa!');

INSERT INTO suspects (name,status,story)
VALUES('Jake',0,'Jake: Hauska tavata! Murha?? Ei kai… Kuinka kamalaa! Olen aivan järkyttynyt… Mitäkö tiedän siitä?\n En.. en mitään, en voi edes ajatella, olen niin kauhuissani. Ajatella, että olen saattanut keskustella murhaajan kanssa!\n Ei, en pysty käsittelemään tätä, en kykene nyt vastaamaan kysymyksiin. {addSuspect} oli tauolla käymässä ulkona, joten hänellä ei ollut tuohon hirmutekoon mahdollisuutta.\n Huh.. Minun pitää nyt päästä pitkälleni, hei hei!');
