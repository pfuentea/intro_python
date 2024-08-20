-- cuantos registros hay?

select count(*)
from INSCRITOS;

-- cuantos inscritos hay en total?

select SUM(cantidad) as total from INSCRITOS;

-- cual o cuales son los registros de mayor antiguedad?

select * from inscritos
where fecha = (select min(fecha) from inscritos);

--cuantos inscritos hay por dia?

select fecha, sum(cantidad) as cantidad_por_dia
from INSCRITOS
group by fecha
order by fecha asc;

-- que dia se inscribieron la mayor cantidad de personas y cuantas fueron ?

select fecha, sum(cantidad) as cantidad_por_dia
from INSCRITOS
group by fecha
order by cantidad_por_dia desc
limit 1;

select fecha, sum(cantidad) as cantidad_por_dia
    from INSCRITOS
    WHERE fecha in (
        select fecha
        from (
            select fecha, sum(cantidad) as cantidad_por_dia
            from INSCRITOS
            group by fecha
        )
        
    )
group by fecha
