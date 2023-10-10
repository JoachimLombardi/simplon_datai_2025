-- On jette on crée
drop database if exists FoodDistribution;
create database FoodDistribution;

-- on utilise
USE FoodDistribution;

CREATE table Famille
(
	ID SMALLINT UNSIGNED NOT NULL auto_increment,
    FAMILLE varchar(30) unique,
    primary key (ID)
);

CREATE table Conditionnement
(
	ID SMALLINT UNSIGNED NOT NULL auto_increment,
    Conditionnement varchar(30) unique,
    primary key (ID)
);

CREATE TABLE Principale
(
	ID INT NOT NULL auto_increment,
    Code_article MEDIUMINT UNSIGNED,
    Libelle VARCHAR(80),
    Famille_ID SMALLINT UNSIGNED NOT NULL,
    Conditionnement_ID SMALLINT UNSIGNED NOT NULL,
    PU_HT DECIMAL (10,2),
    primary key (ID),
    foreign key (Famille_ID) references Famille (ID), 
    foreign key (Conditionnement_ID) references Conditionnement (ID)
);

-- Creation d'une view
CREATE VIEW select_all AS     