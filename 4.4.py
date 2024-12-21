# Nazwa pliku
file_name = 'it_company.csv'

# Funkcja do wyświetlania 5 wierszy na raz
def display_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()  # Wczytujemy wszystkie linie do listy

    total_lines = len(lines)
    start = 0

    # Pętla, która przechodzi po pliku 5 wierszami na raz
    while start < total_lines:
        # Wyświetlamy 5 kolejnych wierszy
        for i in range(start, min(start + 5, total_lines)):
            print(lines[i].strip())  # print bez dodatkowych nowych linii (strip() usuwa \n)

        # Czekamy na naciśnięcie Enter przed wyświetleniem kolejnych wierszy
        input("\nPress Enter key...")

        # Zmieniamy początkowy indeks na kolejne 5 wierszy
        start += 5

# Wywołanie funkcji
display_lines(file_name)
