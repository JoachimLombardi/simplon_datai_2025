DROP DATABASE IF EXISTS sales_data_csv;
CREATE DATABASE sales_data_csv;

USE sales_data_csv;

CREATE TABLE `sales` (
    `date_cmd` DATE  NOT NULL ,
    `day_cmd` int  NOT NULL ,
    `month_cmd` VARCHAR(10)  NOT NULL ,
    `year_cmd` int  NOT NULL ,
    `customer_age` int  NOT NULL ,
    `age_group` VARCHAR(20)  NOT NULL ,
    `customer_gender` VARCHAR(10)  NOT NULL ,
    `country` VARCHAR(15) NOT NULL,
    `state` VARCHAR(20)  NOT NULL ,
    `Product_Category` VARCHAR(15) NOT NULL,
	`Sub_Category` VARCHAR(30) NOT NULL,
    `product` VARCHAR(50)  NOT NULL ,
    `order_quantity` int  NOT NULL ,
    `unit_cost` int  NOT NULL ,
	`Unit_Price` VARCHAR(15) NOT NULL,
    `profit` int  NOT NULL ,
    `cost` int  NOT NULL ,
    `revenue` int  NOT NULL 
);

