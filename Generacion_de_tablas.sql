##Esta tabla es donde se almacenaran los usuarios
DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	id int primary key auto_increment,
	nombre varchar(128),
	id_chat varchar(32) unique,
    plataforma tinyint
);

DROP TABLE IF EXISTS Products;
CREATE TABLE Products(
	id int primary key auto_increment,
    nombre varchar(256),
    descripcion varchar(1024),
    costo double,
    foto varchar(1024),
    enabled boolean
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders(
	id int primary key auto_increment,
    id_user int NOT NULL,
    fecha date,
    telefono varchar(20),
    direccion varchar(256),
    coordenada varchar(32),
    detalles varchar(256),
    checkout double,
    completed boolean,
    
    FOREIGN KEY(id_user) REFERENCES Users(id)
);

DROP TABLE IF EXISTS Discounts;
CREATE TABLE Discounts(
	id int primary key auto_increment,
	id_product int NOT NULL,
	porcentaje float,
    caducidad date,
    enabled boolean,
    
    FOREIGN KEY(id_product) REFERENCES Products(id)
);

DROP TABLE IF EXISTS OrderedProducts;
CREATE TABLE OrderedProducts(
	id int primary key auto_increment,
    id_product int NOT NULL,
    id_order int NOT NULL,
    
    FOREIGN KEY(id_product) REFERENCES Products(id),
    FOREIGN KEY(id_order) REFERENCES Orders(id)
);

DROP TABLE IF EXISTS PermisionTypes;
CREATE TABLE PermisionTypes(
	id int primary key auto_increment,
    rol varchar(128)
);

DROP TABLE IF EXISTS UserPermisions;
CREATE TABLE UserPermisions(
	id int primary key auto_increment,
    id_user int NOT NULL,
    id_permision int NOT NULL,
    
    FOREIGN KEY(id_user) REFERENCES Users(id),
    FOREIGN KEY(id_permision) REFERENCES UserPermisions(id)
);



