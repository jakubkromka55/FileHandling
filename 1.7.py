###
# Reads the entire contents of a file
###
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# Wczytaj całą zawartość pliku i podziel linie na tablicę
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# Oblicz całkowitą liczbę zaparkowanych samochodów
total = 0
for line in file_lines:
   total += int(line)  # Przekształć każdą linię na liczbę i dodaj do sumy

print('Total cars parked:', total)
