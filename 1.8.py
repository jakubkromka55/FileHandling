###
# Reads the entire contents of a file
###
def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

# Wczytaj całą zawartość pliku
file_content = read_from_file('pets.txt')

# Podziel tekst na linie
file_lines = file_content.splitlines()

# Drukuj tekst i licz słowa
total_words = 0

for line in file_lines:
    print(line)  # Wydrukuj linię
    total_words += len(line.split())  # Policz słowa w linii i dodaj do sumy

print('\nTotal number of words:', total_words)
