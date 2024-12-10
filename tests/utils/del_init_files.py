# PARA ELIMINAR TODOS DOS VACIOS
import os

def delete_empty_init_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == "__init__.py":
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) == 0:  # Comprueba si el archivo está vacío
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

if __name__ == "__main__":
    # Cambia '.' por la ruta raíz de tu proyecto si es necesario
    base_directory = "."
    delete_empty_init_files(base_directory)


