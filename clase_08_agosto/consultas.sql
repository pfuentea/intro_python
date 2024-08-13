select * from facturas where importe_total>2500;



select cli.nombre, cli.apellido ,f.importe_total
from clientes as cli
join compras_clientes as cc on (cc.id_cliente=cli.id)
join ventas as v on (cc.id_venta=v.id)
join facturas as f on (f.id= v.id_factura)
where f.importe_total>2500;


insert into compras_clientes(id_venta,id_cliente) values(3,2);

select cli.nombre, cli.apellido ,f.importe_total
from clientes as cli
join compras_clientes as cc on (cc.id_cliente=cli.id)
join ventas as v on (cc.id_venta=v.id)
join facturas as f on (f.id= v.id_factura);
