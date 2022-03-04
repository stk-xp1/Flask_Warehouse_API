
CREATE DATABASE IF NOT EXISTS warehouse;
USE warehouse;


DROP TABLE IF EXISTS products, customers, staff, orders;
CREATE TABLE products (
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(255) NOT NULL,
    amount INT NOT NULL, 
    price FLOAT NOT NULL,
    created_at DATE NULL, 
    updated_at DATE NULL,
    PRIMARY KEY (id)
)ENGINE = InnoDB;

CREATE TABLE customers (
    id INT NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL, 
    street VARCHAR(255) NOT NULL,
    postal_code VARCHAR(255) NOT NULL, 
    age INT NOT NULL, 
    created_at DATE NULL,
    updated_at DATE NULL, 
    PRIMARY KEY (id)
) ENGINE = InnoDB;

CREATE TABLE staffs (
    id INT NOT NULL AUTO_INCREMENT,
    fist_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL, 
    employee_since DATE NULL, 
    age INT NOT NULL,
    created_at DATE NULL,
    updated_at DATE NULL, 
    PRIMARY KEY (id) 
) ENGINE = InnoDB;

CREATE TABLE orders (
   id INT NOT NULL AUTO_INCREMENT,
   product_id INT NOT NULL,
   customer_id INT NOT NULL, 
   staff_id INT NOT NULL, 
   count INT NOT NULL, 
   created_at DATE NULL,
   updated_at DATE NULL, 
   PRIMARY KEY (id),
  CONSTRAINT `product_tbl`
    FOREIGN KEY (`product_id`)
    REFERENCES `warehouse`.`products` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `customer_tbl`
    FOREIGN KEY (`customer_id`)
    REFERENCES `warehouse`.`customers` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `staff_tbl`
    FOREIGN KEY (`staff_id`)
    REFERENCES `warehouse`.`staffs` (`id`)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
) ENGINE = InnoDB;

INSERT INTO products VALUES
    (1001,'Såg',120,13,'2022-01-10','2022-01-10'),
    (1002,'Snus',48,300,'2022-01-10','2022-01-10');


INSERT INTO customers VALUES 
    (101,'Anders','Garcia','Ulla lyckas väg 13',43212,47,'2022-01-10','2022-01-10'),
    (102,'Göran','Persson','Storås vägen 73',41254,29,'2022-01-10','2022-01-10');



INSERT INTO staffs VALUES 
    (1,'Unni','Lozic','2001-10-12',47,'2022-01-10','2022-01-10'),
    (2,'Liv','Strömberg','2012-03-27',32,'2022-01-10','2022-01-10');


INSERT INTO orders VALUES 
    (1,1002,103,1002,1, '2022-01-10','2022-01-10'),
    (2,1004,103,1002,10, '2022-01-10','2022-01-10');
