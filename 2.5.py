# Nazwa pliku listy zakupów
shopping_list = 'shopping_list.txt'

# Funkcja dodająca nazwę produktu do pliku
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')

# Pobieranie kolejnych nazw produktów z klawiatury
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        # Kończy wprowadzanie nazw produktów (przerwanie pętli)
        print("Shopping list creation stopped.")
    else:
        add_product(shopping_list, product)
