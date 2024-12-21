import re  # Importujemy moduł re do pracy z wyrażeniami regularnymi

# Funkcja do liczenia samogłosk w tekście
def count_vowels(text):
    # Wyrażenie regularne do dopasowania samogłosk (małych i wielkich liter)
    vowels_pattern = r'[aeiouAEIOU]'
    vowels = re.findall(vowels_pattern, text)  # Znajdujemy wszystkie samogłoski
    return len(vowels)  # Zwracamy liczbę samogłosk

# Główna część programu
text = input("Wprowadź tekst: ")  # Pobieramy tekst od użytkownika
vowel_count = count_vowels(text)  # Liczymy samogłoski w wprowadzonym tekście

print(f"Liczba samogłosk w tekście: {vowel_count}")  # Wyświetlamy wynik
