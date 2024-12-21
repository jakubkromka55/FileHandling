
def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

# Wczytaj całą zawartość pliku
file_content = read_from_file('countries.txt')

# Podziel zawartość pliku na linie i zapisz je w tablicy
file_lines = file_content.splitlines()

# Posortuj tablicę alfabetycznie
sorted_lines = sorted(file_lines)

# Wypisz posortowaną tablicę
for line in sorted_lines:
    print(line)
