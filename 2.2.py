###
# Zapisuje listę Siedmiu Cudów Świata do pliku w kolejności alfabetycznej
###

# Lista Siedmiu Cudów Świata
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Nazwa pliku, do którego zapiszemy dane
file_name = 'seven_wonders.txt'

# Posortuj dane w kolejności alfabetycznej
seven_wonders.sort()

# Zapisz dane do pliku
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(f"{item}\n")

print(f"Siedem Cudów Świata zostało zapisane do pliku {file_name}.")
