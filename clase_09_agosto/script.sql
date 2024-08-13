create table clientes(
    email varchar(50),
    nombre varchar,
    telefono varchar(16),
    empresa varchar(50),
    prioridad smallint
);

insert into clientes (email,nombre,telefono,empresa,prioridad) values ('correo1@gmail.com','nombre1','999999999','ENEL',2);
insert into clientes (email,nombre,telefono,empresa,prioridad) values ('correo2@gmail.com','nombre2','888888888','AGUAS',4);
insert into clientes (email,nombre,telefono,empresa,prioridad) values ('correo3@gmail.com','nombre3','777777777','CABLE',1);
insert into clientes (email,nombre,telefono,empresa,prioridad) values ('correo4@gmail.com','nombre4','666666666','GAS',10);
insert into clientes (email,nombre,telefono,empresa,prioridad) values ('correo5@gmail.com','nombre5','333333333','AUTOPISTA',8);

 select * from clientes order by prioridad desc limit 3;

 select * from clientes where empresa='GAS' or prioridad=2;

