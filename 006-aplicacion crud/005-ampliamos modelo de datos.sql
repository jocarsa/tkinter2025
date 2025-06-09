-- CLIENTES
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellidos TEXT,
    email TEXT,
    telefono TEXT,
    direccion TEXT
);

-- EMPLEADOS
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellidos TEXT,
    email TEXT,
    telefono TEXT,
    departamento_id INTEGER,
    puesto TEXT,
    salario REAL,
    fecha_contratacion TEXT
);

-- DEPARTAMENTOS (opcional)
CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
);

-- PRODUCTOS
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    descripcion TEXT,
    precio REAL,
    stock INTEGER,
    categoria_id INTEGER
);

-- CATEGORÍAS (opcional)
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
);

-- PEDIDOS
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    fecha TEXT,
    total REAL
);

-- LINEAS DE PEDIDO (relación n-n entre pedidos y productos)
CREATE TABLE IF NOT EXISTS lineas_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    precio_unitario REAL
);
