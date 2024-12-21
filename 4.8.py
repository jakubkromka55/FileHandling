import re  # Importujemy moduł re do pracy z wyrażeniami regularnymi

# Funkcja sprawdzająca, czy rozszerzenie pliku ma dokładnie cztery znaki
def has_four_char_extension(file_name):
    # Używamy wyrażenia regularnego do sprawdzenia rozszerzenia
    match = re.search(r'\.([a-zA-Z0-9]{4})$', file_name)
    return bool(match)  # Zwracamy True, jeśli znaleziono czteroznakowe rozszerzenie

# Główna część programu
try:
    with open('files.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Usuwamy zbędne spacje oraz znaki nowej linii
            if has_four_char_extension(line):
                print(line)  # Drukujemy nazwę pliku, jeśli spełnia warunek
except FileNotFoundError:
    print("Plik 'files.txt' nie został znaleziony.")
