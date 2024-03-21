import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('C:\\Users\\ferna\\DS_thebridge_online\\team challenge grupos\\TeamChallenge_S7_G1_SQL_Game_repository\\challenge bbdd\\g1_farmacia_team_challenge_sprint7.db')
cursor = conn.cursor()

# Insertar registros en la tabla Proveedores
proveedores = [
    (1, 'Proveedor Uno', 'Calle Falsa 123', '555-1234', 'contacto@proveedoruno.com'),
    (2, 'Proveedor Dos', 'Avenida Siempre Viva 456', '555-5678', 'contacto@proveedordos.com'),
    (3, 'Proveedor Tres', 'Ruta 789', '555-9012', 'contacto@proveedortres.com'),
    (4, 'Proveedor Cuatro', 'Avenida Principal 789', '555-3456', 'contacto@proveedorcuatro.com'),
    (5, 'Proveedor Cinco', 'Calle Mayor 456', '555-6789', 'contacto@proveedorcinco.com'),
    (6, 'Proveedor Seis', 'Avenida Central 234', '555-8901', 'contacto@proveedorseis.com'),
    (7, 'Proveedor Siete', 'Calle Secundaria 567', '555-2345', 'contacto@proveedorsiete.com'),
    (8, 'Proveedor Ocho', 'Ruta Perdida 901', '555-6789', 'contacto@proveedorocho.com'),
    (9, 'Proveedor Nueve', 'Avenida Lejana 345', '555-0123', 'contacto@proveedornueve.com'),
    (10, 'Proveedor Diez', 'Calle Remota 678', '555-4567', 'contacto@proveedordiez.com')
]

cursor.executemany('INSERT INTO Proveedores VALUES (?,?,?,?,?)', proveedores)

# Insertar registros en la tabla Productos
productos = [
    (1, 'Producto A', 'Tipo 1', 10.50, 1),
    (2, 'Producto B', 'Tipo 2', 15.75, 9),
    (3, 'Producto C', 'Tipo 1', 12.00, 3),
    (4, 'Producto D', 'Tipo 2', 18.25, 4),
    (5, 'Producto E', 'Tipo 1', 9.99, 4),
    (6, 'Producto F', 'Tipo 2', 20.50, 6),
    (7, 'Producto G', 'Tipo 1', 14.75, 7),
    (8, 'Producto H', 'Tipo 2', 16.80, 7),
    (9, 'Producto I', 'Tipo 1', 11.25, 6),
    (10, 'Producto J', 'Tipo 2', 22.00, 1)
]

cursor.executemany('INSERT INTO Productos VALUES (?,?,?,?,?)', productos)

# Insertar registros en la tabla Stock
stock = [
     (1, 100, '2024-01-20'),
    (2, 75, '2024-03-20'),
    (8, 50, '2022-03-20'),
    (4, 120, '2023-03-20'),
    (5, 200, '2023-05-20'),
    (5, 80, '2024-07-22'),
    (8, 40, '2021-03-10'),
    (8, 150, '2019-12-20'),
    (9, 90, '2024-03-30'),
    (10, 60, '2024-03-26')
]

cursor.executemany('INSERT INTO Stock VALUES (?,?,?)', stock)

# Insertar registros en la tabla Facturas
facturas = [
    (1, 100 * 2.50, 1, '2024-01-20'),
    (2, 75 * 3.25, 2, '2024-03-20'),
    (8, 50 * 4.30, 8, '2022-03-20'),
    (4, 120 * 1.80, 4, '2023-03-20'),
    (5, 200 * 5.10, 5, '2023-05-20'),
    (5, 80 * 2.75, 5, '2024-07-22'),
    (8, 40 * 3.60, 8, '2021-03-10'),
    (8, 150 * 4.90, 8, '2019-12-20'),
    (9, 90 * 6.20, 9, '2024-03-30'),
    (10, 60 * 7.80, 10, '2024-03-26')
]

cursor.executemany('INSERT INTO Facturas VALUES (?,?,?)', facturas)

# Insertar registros en la tabla Detalle_Factura
detalle_factura = [
    (1, 1, 1, 100, '2024-01-20'),
    (2, 2, 2, 75, '2024-03-20'),
    (3, 8, 8, 50, '2022-03-20'),
    (4, 4, 4, 120, '2023-03-20'),
    (5, 5, 5, 200, '2023-05-20'),
    (6, 5, 5, 80, '2024-07-22'),  # Nota: ID_Factura repetido para reflejar la misma factura con diferentes productos
    (7, 8, 8, 40, '2021-03-10'),
    (8, 8, 8, 150, '2019-12-20'), # Nota: ID_Factura repetido para reflejar la misma factura con diferentes productos
    (9, 9, 9, 90, '2024-03-30'),
    (10, 10, 10, 60, '2024-03-26')
]

cursor.executemany('INSERT INTO Detalle_Factura VALUES (?,?,?,?,?)', detalle_factura)

# Guardar los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()

print("Registros insertados exitosamente.")