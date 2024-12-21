# Funkcja obliczająca liczbę wierszy, znaków i słów w pliku
def count_file_content(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Odczytujemy wszystkie linie
            num_lines = len(lines)  # Liczba wierszy
            num_chars = sum(len(line) for line in lines)  # Liczba znaków
            num_words = sum(len(line.split()) for line in lines)  # Liczba słów
            return num_lines, num_chars, num_words
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None

# Główna część programu
file_name = input("Enter the file name: ")  # Pobieranie nazwy pliku od użytkownika

result = count_file_content(file_name)  # Obliczanie danych

if result:  # Jeśli wynik nie jest None
    num_lines, num_chars, num_words = result
    print(f"File name: {file_name}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_chars}")
    print(f"Number of words: {num_words}")
