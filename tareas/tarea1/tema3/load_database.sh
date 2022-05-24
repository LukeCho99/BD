#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 $DIR/tablas/create_database.py
python3 $DIR/tablas/direcciones.py
python3 $DIR/tablas/polideportivo.py
python3 $DIR/tablas/unico.py
python3 $DIR/tablas/mapas.py
python3 $DIR/tablas/eventos.py
python3 $DIR/tablas/roles.py
