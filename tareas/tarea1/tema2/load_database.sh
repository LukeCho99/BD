#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 $DIR/tablas/create_database.py
python3 $DIR/tablas/clientes.py
python3 $DIR/tablas/direcciones.py
python3 $DIR/tablas/productos.py
python3 $DIR/tablas/telefonos.py
python3 $DIR/tablas/ventas.py
python3 $DIR/tablas/categorias.py
python3 $DIR/tablas/proveedores.py
python3 $DIR/tablas/infoventas.py
