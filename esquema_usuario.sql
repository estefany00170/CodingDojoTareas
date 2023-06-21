#Consulta: crea 3 usuarios nuevos
INSERT INTO usuarios(nombre, apellido, email)
VALUES  ('Amy', 'Caceres', 'amy@caceres.com'),
		('Paula', 'Nuñez', 'paula@nuñez.com'),
		('Felipe', 'Perez', 'felipe@perez.com');
#Consulta: recupera todos los usuarios
SELECT *
FROM usuarios;

#Consulta: recupera el primer usuario usando su dirección de correo electrónico
SELECT *
FROM usuarios
WHERE email = 'amy@caceres.com';

#Consulta: recupera el último usuario usando su id
SELECT *
FROM usuarios
WHERE id = 3;

#Consulta: cambia el usuario con id=3 para que su apellido sea Panqueques
UPDATE usuarios
SET apellido = 'Panqueques'
WHERE id = 3;

#Consulta: elimina el usuario con id=2 de la base de datos
DELETE FROM usuarios
WHERE id = 2;

#Consulta: obtén todos los usuarios, ordenados por su nombre
SELECT *
FROM usuarios
ORDER BY nombre;

#Consulta BONUS: obtén todos los usuarios, ordenados por su nombre en orden descendente
SELECT *
FROM usuarios
ORDER BY nombre DESC;


