import re  # moduł do wyrażeń regularnych

# Nazwa pliku z raportem zakupów
email_file = 'report.txt'

# Funkcja do obliczenia całkowitej wartości wydanych pieniędzy
def calculate_total_spent(file_name):
    # Otwieramy plik w trybie odczytu z kodowaniem UTF-8
    with open(file_name, 'r', encoding='utf-8') as file:
        # Odczytujemy zawartość pliku
        email_content = file.read()

    # Wzór wyrażenia regularnego do wyszukiwania kwot z symbolem euro
    # Obsługuje formaty takie jak €102.00 i €102,00
    pattern = r'€(\d+[\.,]?\d*)'

    # Znajdujemy wszystkie kwoty w tekście
    amounts = re.findall(pattern, email_content)

    # Przekształcamy kwoty na liczby zmiennoprzecinkowe i sumujemy je
    total_spent = 0.0
    for amount in amounts:
        # Zamiana przecinka na kropkę w kwocie, by mogła zostać przekonwertowana na float
        amount = amount.replace(',', '.')
        total_spent += float(amount)

    return total_spent

# Obliczanie całkowitej wydanej kwoty
total = calculate_total_spent(email_file)

# Wyświetlanie wyniku
print(f"Całkowita wartość wydanych pieniędzy: €{total:.2f}")
