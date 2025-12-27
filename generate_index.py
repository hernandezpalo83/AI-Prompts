import os
import json

def generate_index():
    data_folder = 'data'
    all_prompts = []

    # Verificar si la carpeta data existe
    if not os.path.exists(data_folder):
        print(f"Error: La carpeta '{data_folder}' no existe.")
        return

    # Leer cada archivo JSON en la carpeta data
    for filename in os.listdir(data_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(data_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_prompts.extend(data)
                except json.JSONDecodeError:
                    print(f"Error al leer {filename}. Formato JSON no válido.")

    # Guardar el índice final
    with open('index.json', 'w', encoding='utf-8') as f:
        json.dump(all_prompts, f, indent=2, ensure_ascii=False)
    
    print(f"✅ index.json generado con éxito con {len(all_prompts)} prompts.")

if __name__ == "__main__":
    generate_index()