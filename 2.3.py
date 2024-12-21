# Nazwy plików
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Odczytanie zawartości oryginalnego pliku
with open(original_file, 'r') as original:
    content = original.read()

# Zapisanie zawartości do pliku docelowego (kopii)
with open(target_file, 'w') as target:
    target.write(content)
