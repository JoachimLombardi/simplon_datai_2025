DROP DATABASE IF EXISTS commandes_data;
CREATE DATABASE commandes_data;

USE commandes_data;

CREATE TABLE `Commande` (
    `Id` INT  NOT NULL ,
    `ID_Client` INT  NOT NULL ,
    `ID_Commande` INT  NOT NULL ,
    `Date_Commande` DATE  NOT NULL ,
    `Montant_Commande` FLOAT  NOT NULL ,
    `Adresse_Id` INT  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Commande_Produit` (
    `Id` INT  NOT NULL ,
    `Commandes_Id` INT  NOT NULL ,
    `Id_Produit` INT  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Client` (
    `Id` INT  NOT NULL ,
    `Email` VARCHAR(30)  NOT NULL ,
    `Nom` VARCHAR(10)  NOT NULL ,
    `Prenom` VARCHAR(10)  NOT NULL ,
    `Adresse_id` INT  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Adresse` (
    `Id` INT  NOT NULL ,
    `Adresse` VARCHAR(30)  NOT NULL ,
    `Ville_Id` INT  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Ville` (
    `Id` INT  NOT NULL ,
    `Nom` VARCHAR(10)  NOT NULL ,
    `Pays_Id` INT  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Pays` (
    `Id` INT  NOT NULL ,
    `Nom` VARCHAR(10)  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Categorie` (
    `Id` INT  NOT NULL ,
    `Category` VARCHAR(15)  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

CREATE TABLE `Produit` (
    `Id` INT  NOT NULL ,
    `Nom` VARCHAR(10)  NOT NULL ,
    `Categorie_Id` INT  NOT NULL ,
    PRIMARY KEY (
        `Id`
    )
);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_ID_Client` FOREIGN KEY(`ID_Client`)
REFERENCES `Client` (`Id`);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_Adresse_Id` FOREIGN KEY(`Adresse_Id`)
REFERENCES `Adresse` (`Id`);

ALTER TABLE `Commande_Produit` ADD CONSTRAINT `fk_Commande_Produit_Commandes_Id` FOREIGN KEY(`Commandes_Id`)
REFERENCES `Commande` (`Id`);

ALTER TABLE `Commande_Produit` ADD CONSTRAINT `fk_Commande_Produit_Id_Produit` FOREIGN KEY(`Id_Produit`)
REFERENCES `Produit` (`Id`);

ALTER TABLE `Client` ADD CONSTRAINT `fk_Client_Adresse_id` FOREIGN KEY(`Adresse_id`)
REFERENCES `Adresse` (`Id`);

ALTER TABLE `Adresse` ADD CONSTRAINT `fk_Adresse_Ville_Id` FOREIGN KEY(`Ville_Id`)
REFERENCES `Ville` (`Id`);

ALTER TABLE `Ville` ADD CONSTRAINT `fk_Ville_Pays_Id` FOREIGN KEY(`Pays_Id`)
REFERENCES `Pays` (`Id`);

ALTER TABLE `Produit` ADD CONSTRAINT `fk_Produit_Categorie_Id` FOREIGN KEY(`Categorie_Id`)
REFERENCES `Categorie` (`Id`);

