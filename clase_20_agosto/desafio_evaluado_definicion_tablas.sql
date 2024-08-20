create database peliculas;

create table peliculas(
    id int primary key,
    titulo varchar(100),
    year int,
    director varchar(100)
);

create table reparto(
    id_pelicula int,
    actor varchar(100),
    foreign key (id_pelicula) references peliculas(id)
);

\copy peliculas(id,titulo,year,director) FROM 'peliculas.csv' DELIMITER ',' CSV HEADER;

\copy reparto(id_pelicula,actor) FROM 'reparto.csv' DELIMITER ',' CSV HEADER;

 select * from peliculas where titulo='Titanic';

select r.actor 
from peliculas as p
join reparto as r on (p.id=r.id_pelicula)
where p.titulo='Titanic';

select count(*)
from peliculas as p
join reparto as r on (p.id=r.id_pelicula)
where r.actor='Harrison Ford';

select *
from peliculas as p
where year >=1990 and year <2000
order by titulo asc;

select titulo ,  LENGTH(titulo)  as longitud_titulo
from peliculas as p;

select titulo ,  LENGTH(titulo)  as longitud_titulo
from peliculas as p
order by longitud_titulo desc
limit 1;
