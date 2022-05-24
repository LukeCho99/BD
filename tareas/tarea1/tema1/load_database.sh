#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 $DIR/tablas/create_database.py
python3 $DIR/tablas/clientes.py
python3 $DIR/tablas/direcciones.py
python3 $DIR/tablas/articulos.py
python3 $DIR/tablas/fabricas.py
python3 $DIR/tablas/inventario.py
python3 $DIR/tablas/pedidos.py
python3 $DIR/tablas/cuerpos.py
