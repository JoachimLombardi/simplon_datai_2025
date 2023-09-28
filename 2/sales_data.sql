DROP DATABASE IF EXISTS sales_data;
CREATE DATABASE sales_data;

USE sales_data;

CREATE TABLE `Mois` (
    `ID` int  NOT NULL AUTO_INCREMENT, 
    `month` varchar(10)  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Age_Group` (
    `ID` int  NOT NULL AUTO_INCREMENT,
    `age_group` varchar(20)  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Customer_Gender` (
    `ID` int  NOT NULL AUTO_INCREMENT,
    `customer_gender` varchar(10)  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Country` (
    `ID` int  NOT NULL AUTO_INCREMENT,
    `country` varchar(20)  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Product_Category` (
    `ID` int  NOT NULL AUTO_INCREMENT,
    `product_category` varchar(50)  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `State` (
    `ID` int AUTO_INCREMENT,
    `state` varchar(20)  NOT NULL ,
    `country` int ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Sub_Category` (
    `ID` int AUTO_INCREMENT,
    `sub_category` varchar(50)  NOT NULL ,
    `product_category` int ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Product` (
    `ID` int AUTO_INCREMENT,
    `product` varchar(50)  NOT NULL ,
    `sub_category` int ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Commande` (
    `ID` int AUTO_INCREMENT,
    `date_cmd` DATE  NOT NULL ,
    `day_cmd` int  NOT NULL ,
    `month_cmd` int ,
    `year_cmd` int  NOT NULL ,
    `customer_age` int  NOT NULL ,
    `age_group` int ,
    `customer_gender` int ,
    `state` int ,
    `product` int ,
    `order_quantity` int  NOT NULL ,
    `unit_cost` int  NOT NULL ,
    `profit` int  NOT NULL ,
    `cost` int  NOT NULL ,
    `revenue` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

ALTER TABLE `State` ADD CONSTRAINT `fk_State_country` FOREIGN KEY(`country`)
REFERENCES `Country` (`ID`);

ALTER TABLE `Sub_Category` ADD CONSTRAINT `fk_Sub_Category_product_category` FOREIGN KEY(`product_category`)
REFERENCES `Product_Category` (`ID`);

ALTER TABLE `Product` ADD CONSTRAINT `fk_Product_sub_category` FOREIGN KEY(`sub_category`)
REFERENCES `Sub_Category` (`ID`);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_month_cmd` FOREIGN KEY(`month_cmd`)
REFERENCES `Mois` (`ID`);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_age_group` FOREIGN KEY(`age_group`)
REFERENCES `Age_Group` (`ID`);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_customer_gender` FOREIGN KEY(`customer_gender`)
REFERENCES `Customer_Gender` (`ID`);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_state` FOREIGN KEY(`state`)
REFERENCES `State` (`ID`);

ALTER TABLE `Commande` ADD CONSTRAINT `fk_Commande_product` FOREIGN KEY(`product`)
REFERENCES `Product` (`ID`);

