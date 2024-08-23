-- req 1

create table peliculas(
    id serial primary key, -- primary key == not null y unique
    nombre varchar(255) NOT NULL,
    anno int NOT NULL
);


create table tags(
    id SERIAL PRIMARY KEY,
    tag varchar(32)  NOT NULL
);

create table peliculas_tags(
    id SERIAL PRIMARY KEY,
    pelicula_id INT REFERENCES peliculas(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE
);

-- req 2
INSERT INTO peliculas (id, nombre, anno) VALUES (1, 'The Matrix', 1999);
INSERT INTO peliculas (id, nombre, anno) VALUES (2, 'Inception', 2010);
INSERT INTO peliculas (id, nombre, anno) VALUES (3, 'Interstellar', 2014);
INSERT INTO peliculas (id, nombre, anno) VALUES (4, 'The Godfather', 1972);
INSERT INTO peliculas (id, nombre, anno) VALUES (5, 'Pulp Fiction', 1994);

INSERT INTO tags (id, tag) VALUES (1, 'Sci-Fi');
INSERT INTO tags (id, tag) VALUES (2, 'Thriller');
INSERT INTO tags (id, tag) VALUES (3, 'Drama');
INSERT INTO tags (id, tag) VALUES (4, 'Action');
INSERT INTO tags (id, tag) VALUES (5, 'Adventure');

INSERT INTO peliculas_tags(pelicula_id,tag_id) VALUES (1,1);
INSERT INTO peliculas_tags(pelicula_id,tag_id) VALUES (1,4);
INSERT INTO peliculas_tags(pelicula_id,tag_id) VALUES (1,5);

INSERT INTO peliculas_tags(pelicula_id,tag_id) VALUES (2,1);
INSERT INTO peliculas_tags(pelicula_id,tag_id) VALUES (2,4);


-- req 3
SELECT p.nombre, count(pt.tag_id)
FROM peliculas as p
LEFT JOIN peliculas_tags as pt ON (p.id=pt.pelicula_id)
GROUP BY p.nombre;

-- req 4
CREATE TABLE preguntas(
    id serial primary key,
    pregunta varchar(255) not null,
    respuesta_correcta varchar not null
);

CREATE TABLE usuarios(
    id serial primary key,
    nombre varchar(255) not null,
    edad int not null
);

CREATE TABLE respuestas(
    id serial primary key,
    respuesta varchar(255) not null,
    usuario_id  int REFERENCES usuarios(id) ON DELETE CASCADE,
    pregunta_id  int REFERENCES preguntas(id) ON DELETE CASCADE
);

-- req 5
INSERT INTO preguntas (pregunta, respuesta_correcta) VALUES
('¿Cuál es la capital de Francia?', 'París'),
('¿En qué año llegó el hombre a la Luna?', '1969'),
('¿Quién escribió "Cien años de soledad"?', 'Gabriel García Márquez'),
('¿Cuál es el metal más abundante en la corteza terrestre?', 'Aluminio'),
('¿Quién pintó la Mona Lisa?', 'Leonardo da Vinci');

INSERT INTO usuarios (nombre, edad) VALUES
('Carlos Pérez', 28),
('María López', 22),
('Ana Gómez', 35),
('Jorge Sánchez', 30),
('Lucía Ramírez', 25);

INSERT INTO respuestas (respuesta, usuario_id,pregunta_id)
VALUES ('París',2,1)  , ('París',4,1) , ('1969',3,2),('Cobre',3,4),('Piccaso',3,5);


-- req 6
SELECT u.nombre ,count(p.respuesta_correcta) total_correctas
FROM usuarios AS u
LEFT JOIN respuestas AS r ON (u.id=r.usuario_id)
LEFT JOIN preguntas as p ON (r.respuesta=p.respuesta_correcta)
group by u.nombre;

-- req 7
SELECT p.pregunta, count(r.usuario_id) usuarios_correctos
FROM preguntas as p
LEFT JOIN respuestas as r ON (r.respuesta=p.respuesta_correcta)
LEFT JOIN usuarios AS u ON (u.id=r.usuario_id)
group by p.pregunta;

--req 8 
DELETE FROM usuarios WHERE id=1;

-- req 9

ALTER TABLE usuarios ADD CONSTRAINT mayor_edad CHECK (edad>=18);

--req 10

ALTER TABLE usuarios ADD COLUMN email varchar(255) unique;



