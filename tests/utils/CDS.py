import sqlite3
import os

# Obtener la ruta de la base de datos desde las variables de entorno
db_path = os.getenv("DB_FULL_PATH", "data/app.db")

# Conexión a la base de datos
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar el comando PRAGMA compile_options
    cursor.execute("PRAGMA compile_options;")
    options = cursor.fetchall()

    # Mostrar las opciones de compilación de SQLite
    print("Opciones de compilación de SQLite:")
    for option in options:
        print(option[0])

except sqlite3.Error as e:
    print(f"Error al conectar con la base de datos: {e}")
finally:
    if conn:
        conn.close()

# Malas noticias el peewee no admite el json para sqlite
# o mejor dicho, es culpa del sqlite