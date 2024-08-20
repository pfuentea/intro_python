-- El cliente nos solicita un pequeño reporte de pruebas 
-- donde se registren el
-- nombre de todos los viajeros con y sin boletos, 
-- el número de boleto (para los casos
-- que correspondan) y el nombre del destino.
select v.nombre,t.numero_boleto,d.nombre_destino 
from viajeros as v 
left join tickets as t on (t.viajero_id=v.viajero_id) 
left join destinos as d on (d.destino_id=t.destino_id);

INSERT INTO Tickets (viajero_id, destino_id, numero_boleto, fecha_emision, fecha_salida, fecha_retorno) VALUES
(4, 3, 'T171717', '2024-01-04', '2024-03-28', '2024-04-01'),
(10, 5, 'T8888888', '2024-01-04', '2024-03-28', '2024-04-01'),
(7, 4, 'T202020', '2024-01-04', '2024-03-28', '2024-04-01');

DELETE FROM Tickets where ticket_id=4;
DELETE FROM Viajeros where viajero_id=2;
DELETE FROM destinos where destino_id=5;

CREATE TABLE Paises(
    pais_id SERIAL PRIMARY KEY, 
    nombre_pais  VARCHAR(100) NOT NULL, 
    ciudad  VARCHAR(100) ,
    codigo_postal  VARCHAR(100) NOT NULL
);

insert into paises(ciudad,nombre_pais, codigo_postal) 
values ('Playa del Carmen','México','1239871'),
('Puerto Natales','Chile','3339871'),
('Marrakech','Marruecos','3339871'),
('Santorini','Grecia','3339871'),
('Khumbu','Nepal','3339871'),
('Queensland','Australia','3339871'),
('Kioto','Japon','3339871'),
('Cuzco','Peru','3339871');

--  Modifica la tabla Destinos para agregar el pais_id como FK

ALTER TABLE destinos add column pais_id bigint;
ALTER TABLE destinos add constraint fk_pais_id foreign key (pais_id) references paises(pais_id) ON DELETE CASCADE;

-- Actualiza la tabla Destinos para que coincidan los pais_id en ambas tablas según el nombre de destino.




select * from destinos as d join paises as p on (d.ciudad=p.ciudad);

-- query para actualizar los id_pais en destinos
update destinos d
set pais_id=p.pais_id
from  paises as p 
where (d.ciudad=p.ciudad)
;

-- Borra las columnas país y ciudad de la tabla Destinos 
ALTER TABLE destinos DROP COLUMN ciudad;
ALTER TABLE destinos DROP COLUMN pais;

-- Mostrar la información del boleto T123456 junto con los detalles del viajero y destino
 correspondienteaeseboleto.
select v.*,t.*,d.* from viajeros as v 
left join tickets as t on (t.viajero_id=v.viajero_id) 
left join destinos as d on (d.destino_id=t.destino_id)
where numero_boleto='T123456';

--  Listar todos los viajeros que tienen fecha de salida o de retorno el '2024-01-10'
select v.*
from viajeros as v
left join tickets as t on (t.viajero_id=v.viajero_id) 
where t.fecha_salida='2024-01-10' OR t.fecha_retorno='2024-01-10';

--Obtener el número total de boletos por cada género

select v.genero, count(*) as total
from tickets as t
join viajeros as v on (t.viajero_id=v.viajero_id) 
group by v.genero;

--Obtener un listado de todos los viajeros 
-- que han viajado a Playa del Carmen

select v.nombre
from viajeros as v 
left join tickets as t on (t.viajero_id=v.viajero_id) 
left join destinos as d on (d.destino_id=t.destino_id)
left join paises as p on (d.pais_id=p.pais_id) 
where p.ciudad='Playa del Carmen';
