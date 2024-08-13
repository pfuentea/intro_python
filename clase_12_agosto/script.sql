-- este es un comentario
-- creamos la BD
create database comidas_tipicas;
-- nos conectamos a la BD
\c comidas_tipicas
-- creamos nuestra tabla para trabajar en ella
create table cocina_chilena(id int, nombre varchar(50));
-- DML
-- OJO: las instrucciones deben terminar siempre con punto y coma ";"
-- INSERT 
-- podemos insertar registros 1 x 1 
INSERT INTO cocina_chilena(id, nombre) VALUES ('1','Pastel de choclo');
-- podemos insertar varios registros al mismo tiempo, separados por coma
INSERT INTO cocina_chilena(id, nombre) VALUES ('2', 'Humitas') , ('3','Cazuela') ,('4','Charquican') ;

INSERT INTO cocina_chilena(id, nombre) VALUES ('5','Polotos con Liendas');
-- Nos aseguramos que el registro con id=5 es el que tiene un error
-- SELECT 
SELECT * FROM cocina_chilena WHERE id=5;

-- Para remediar el problema usaremos la instrucción UPDATE

UPDATE cocina_chilena SET nombre='Porotos con Riendas' WHERE id=5;

ALTER TABLE cocina_chilena ADD COLUMN autor varchar(50) default '';

UPDATE cocina_chilena SET autor='Master Chef' WHERE id in (3,4) ;

UPDATE cocina_chilena SET autor='Anonimo' WHERE autor ='';

-- por defecto las tablas están desordenadas. 
-- Para obtener un resultado ordenado usamos ORDER_BY al final del select
SELECT * FROM cocina_chilena ORDER BY id ; -- por defecto el ORDER es ascendente

-- si quiero ordenar por autor y luego por nombre:

SELECT * FROM cocina_chilena ORDER BY autor,nombre;

--insertamos un registro con errores:
INSERT INTO cocina_chilena (id, nombre,autor) VALUES ('7','Pizza','Luigi');

-- DELETE
-- 1.- buscan el registro que quieren borrar
SELECT * FROM cocina_chilena WHERE id=7;
-- 2.- Cambian "SELECT *" por "DELETE"
DELETE FROM cocina_chilena WHERE id=7;

INSERT INTO cocina_chilena (id, nombre,autor) VALUES (2147483647,'Pizza','Luigi');

INSERT INTO cocina_chilena (id, nombre,autor) VALUES (2147483648,'Wantan','Huan');










