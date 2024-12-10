# python add_init_files.py
# A veces me han desaparecido los __init__.py, esto los vuelve a crear

import os

def list_all_directories(base_dir,exclude_dirs):
    # Lista para almacenar los nombres de las carpetas
    all_directories = []

    # Recorre el directorio y sus subdirectorios
    for root, dirs, files in os.walk(base_dir):
        if not any(subcadena in root for subcadena in exclude_dirs):
            # print(root)
            if root != ".":
                init_file = os.path.join(root, "__init__.py")
                if not os.path.exists(init_file):
                    open(init_file, 'a').close()
                    print(f"Created: {init_file}")

if __name__ == "__main__":
    base_directory = "."  # Cambia esto por el directorio base que desees

    # Lista de carpetas a excluir
    exclude_directories = [
        "envCV",
        "templates",
        "exports",
        "logs",
        ".git", # ".git" peta
        ".vscode",
        "__pycache__"
    ]

    list_all_directories(base_directory, exclude_directories)


