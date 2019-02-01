drop database przychodnia;


Create database przychodnia;
use przychodnia;



create table if not exists pacjenci
( 
id 						int primary key AUTO_INCREMENT,
imie 					VARCHAR(15) NOT NULL,
nazwisko 				VARCHAR(15) NOT NULL,
data_ur					date not NULL,
pesel					VARCHAR(15) NOT NULL UNIQUE,
haslo					VARCHAR(15) NOT NULL,
funkcja					VARCHAR(10) DEFAULT 'pacjent'
);

create table if not exists lekarze
( 
id_lek					int primary key AUTO_INCREMENT,
imie_lek 				VARCHAR(15) NOT NULL,
nazwisko_lek			VARCHAR(15) NOT NULL,
specjalizacja			VARCHAR(15) NOT NULL,
pesel_lek				VARCHAR(15) NOT NULL UNIQUE,
haslo_lek				VARCHAR(15) NOT NULL,
funkcja					VARCHAR(10) DEFAULT 'lekarz'
);

Create table if not exists wizyty
(
nr_wizyty						int primary key AUTO_INCREMENT,
id_pacjenta						int not null,
id_lekarza						int not null,
data_wizyty						DATE,
FOREIGN KEY (id_pacjenta) 		REFERENCES pacjenci(id), 
FOREIGN KEY (id_lekarza) 		REFERENCES lekarze(id_lek)
);

Create table if not exists przepisane_leki
(
nr_wizyty						int not null UNIQUE,
nazwa_leku						VARCHAR(25),
FOREIGN KEY (nr_wizyty) 		REFERENCES wizyty(nr_wizyty)
);
show tables;

insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Andrzej','Hajczuk', '1953-03-10', 53031058762, 'lala');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Antoni','Domińczak', '1962-08-15', 62081558762,'qaz');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Jan','Falkiewicz', '1969-11-02', 69110258762,'wsx');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Antoni', 'Gielnik', '1988-06-24', 88062458762,'edc');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Ryszard','Gnacikowska', '1993-01-30', 93013058762,'rfv');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Jan','Bilski', '1975-12-03', 75120358762,'tgb');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Marian','Borowiec', '1981-07-13', 81071358762,'yhn');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Janusz','Basiński', '1999-03-22', 99032258762,'ujm');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Zdzisław','Domżał', '1958-12-17', 58121758762,'iop');
insert into pacjenci (id, imie, nazwisko, data_ur, pesel,haslo) values (id,'Andrzej','Jakubowski', '1978-04-18', 78041858762,'plk');

insert into lekarze values (id_lek,'Jerzy', 'Fejkowski', "chirurg",84112375930,'haslo0',funkcja);
insert into lekarze (id_lek, imie_lek, nazwisko_lek, specjalizacja,pesel_lek,haslo_lek) values (id_lek,'Andrzej','Jabłoński', "internista",12345678999,'haslo1');
insert into lekarze (id_lek, imie_lek, nazwisko_lek, specjalizacja,pesel_lek,haslo_lek) values (id_lek,'Jolanta', 'Gawęcka', "pediatra",57042912345,'haslo2');
insert into lekarze (id_lek, imie_lek, nazwisko_lek, specjalizacja,pesel_lek,haslo_lek) values (id_lek,'Jolanta', 'Gąsiorek', "kardiolog",66021298765,'haslo3');
insert into lekarze (id_lek, imie_lek, nazwisko_lek, specjalizacja,pesel_lek,haslo_lek) values (id_lek,'Adam', 'Brzyska', "psycholog",76012245637,'haslo4');
insert into lekarze (id_lek, imie_lek, nazwisko_lek, specjalizacja,pesel_lek,haslo_lek) values (id_lek,'Anna', 'Chylińska', "anestezjolog",82121304678,'haslo5');
insert into lekarze (id_lek, imie_lek, nazwisko_lek, specjalizacja,pesel_lek,haslo_lek) values (id_lek,'Piotr', 'Gradzik', "dermatolog",91093078940,'haslo6');


Insert into wizyty (id_pacjenta,id_lekarza, data_wizyty) values (10,2,'15-08-07');
Insert into wizyty values (nr_wizyty,8,1,'14-06-05');
Insert into wizyty values (nr_wizyty,8,5,'28-02-07');
Insert into wizyty values (nr_wizyty,3,3,'20-05-05');
Insert into wizyty values (nr_wizyty,5,7,'16-11-06');
Insert into wizyty values (nr_wizyty,9,4,'01-07-05');
Insert into wizyty values (nr_wizyty,1,6,'01-05-07');
Insert into wizyty values (nr_wizyty,4,2,'13-08-05');
Insert into wizyty values (nr_wizyty,1,5,'15-01-07');
Insert into wizyty values (nr_wizyty,6,7,'12-01-07');
Insert into wizyty values (nr_wizyty,7,2,'02-02-05');
Insert into wizyty values (nr_wizyty,3,5,'15-08-05');
Insert into wizyty values (nr_wizyty,1,2,'24-11-05');
Insert into wizyty values (nr_wizyty,9,6,'03-09-05');
Insert into wizyty values (nr_wizyty,10,3,'19-12-05');
Insert into wizyty values (nr_wizyty,5,2,'24-01-06');
Insert into wizyty values (nr_wizyty,6,6,'05-05-07');
Insert into wizyty values (nr_wizyty,2,4,'18-09-06');
Insert into wizyty values (nr_wizyty,7,7,'12-03-05');
Insert into wizyty values (nr_wizyty,8,1,'18-04-05');

#baza  lekow https://bazalekow.mp.pl/leki/items.html?letter=B
Insert into przepisane_leki values (1,'Acard');
Insert into przepisane_leki values (2,'Acatar');
Insert into przepisane_leki values (3,'Bactrim');
Insert into przepisane_leki values (4,'Bebilon');
Insert into przepisane_leki values (5,'Cerutin');
Insert into przepisane_leki values (6,'D-Vitum Forte');
Insert into przepisane_leki values (7,'Etopiryna');
Insert into przepisane_leki values (8,'Fervex');
Insert into przepisane_leki values (9,'Gripex');
Insert into przepisane_leki values (10,'Ibuprofen');
Insert into przepisane_leki values (11,'Melisa fix');
Insert into przepisane_leki values (12,'Polopiryna C');
Insert into przepisane_leki values (13,'Polocard');
Insert into przepisane_leki values (14,'Rutinoscorbin');
Insert into przepisane_leki values (15,'Ranigast');
Insert into przepisane_leki values (16,'RedBlocker');
Insert into przepisane_leki values (17,'Szałwia');
Insert into przepisane_leki values (18,'Theraflu MaxGRIP');
Insert into przepisane_leki values (19,'Xyzal');
Insert into przepisane_leki values (20,'Zyrtec');


#########################################################################################################################################################################################
Create VIEW szczegoly_wizyty as SELECT nr_wizyty, data_wizyty, id_pacjenta, pac.imie, pac.pesel, pac.nazwisko,id_lekarza, lek.specjalizacja, lek.imie_lek,lek.nazwisko_lek from wizyty as wiz 
left JOIN lekarze as lek on wiz.id_lekarza=lek.id_lek left join pacjenci as pac on wiz.id_pacjenta=pac.id ;
#########################################################################################################################################################################################
CREATE VIEW leki_pacjentow AS SELECT wiz.nr_wizyty,pac.id as 'id_pacjenta', wiz.id_lekarza, lekarze.specjalizacja, lekarze.imie_lek,lekarze.nazwisko_lek,pac.imie, pac.nazwisko, pac.pesel, prze.nazwa_leku from przepisane_leki as prze 
left join wizyty as wiz on prze.nr_wizyty=wiz.nr_wizyty left join pacjenci=pac on wiz.id_pacjenta=pac.id left join lekarze on wiz.id_lekarza=lekarze.id_lek;
#########################################################################################################################################################################################
#ilosc wizyt poszczegolnego lekarza
CREATE View suma_wizyt_pojedynczego_lekarza AS
select count(*) as ilosc_wizyt, lekarze.imie_lek, lekarze.nazwisko_lek, lekarze.specjalizacja from lekarze right join wizyty on  lekarze.id_lek= wizyty.id_lekarza group by id_lekarza ;
#########################################################################################################################################################################################
CREATE VIEW pacjenci_bez_lekow AS SELECT wiz.nr_wizyty,pac.id as 'id_pacjenta', wiz.id_lekarza, lekarze.specjalizacja, lekarze.imie_lek,lekarze.nazwisko_lek,pac.imie, pac.nazwisko, pac.pesel, prze.nazwa_leku from przepisane_leki as prze 
right join wizyty as wiz on prze.nr_wizyty=wiz.nr_wizyty left join pacjenci=pac on wiz.id_pacjenta=pac.id left join lekarze on wiz.id_lekarza=lekarze.id_lek;
#########################################################################################################################################################################################
SELECT * from pacjenci;
SELECT * from lekarze;
SELECT * from wizyty;
SELECT * from przepisane_leki;
SELECT * from szczegoly_wizyty;
SELECT * from leki_pacjentow;
Select * from suma_wizyt_pojedynczego_lekarza;
SELECT * from pacjenci_bez_lekow;

#SELECT nr_wizyty, imie, nazwa_leku, nazwisko, pesel FROM pacjenci_bez_lekow where id_lekarza = 1 and nazwa_leku is NULL;


#########################################################################################################################################################################################
#Alter table lekarze modify specjalizacja Varchar(15) not null after id_lek;
#########################################################################################################################################################################################
#Update pacjenci set nazwisko = "Adamski" where id = 2;

# ALTER TABLE table_name MODIFY password varchar(20) AFTER id zapytanie do PYTHON
#chce aby lekarz podawal swoja dostepnosc i wowczas pacjent mogl sie do niego zapisac;
#dodatkowo baza pacjenci ma pokazac czy taki pacjent byl juz u danego lekarza w przeszlosci, jesli tak to podac date wizyty;

