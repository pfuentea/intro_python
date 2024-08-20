create table clientes (
    id int unique not null primary key, 
    nombre varchar not null, 
    rut varchar unique not null
);
