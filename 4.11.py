# Funkcja do obliczania i zapisywania potęg liczb do pliku
def calculate_and_save_powers():
    # Otwarcie pliku do zapisu
    with open('powers.txt', 'w') as file:
        # Iterowanie po liczbach od 1 do 100
        for i in range(1, 101):
            # Obliczanie drugiej i trzeciej potęgi
            square = i ** 2
            cube = i ** 3
            # Tworzenie linii z danymi
            line = f"{i},{square},{cube}\n"
            # Zapisywanie do pliku
            file.write(line)
            # Drukowanie na ekran
            print(line, end='')

# Wywołanie funkcji
calculate_and_save_powers()
