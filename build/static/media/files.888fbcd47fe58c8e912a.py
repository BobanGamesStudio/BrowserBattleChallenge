import os

def list_image_files():
    try:
        # Pobranie bieżącej ścieżki
        current_path = os.path.dirname(os.path.abspath(__file__))
        
        # Pobranie listy plików w bieżącym katalogu
        files = os.listdir(current_path)
        
        # Filtracja plików, aby wybrać tylko te z rozszerzeniem obrazu
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        
        # Wypisanie nazw plików obrazów
        for image_file in image_files:
            print(image_file)
    except Exception as e:
        print("Wystąpił błąd:", e)

# Wywołanie funkcji
list_image_files()
