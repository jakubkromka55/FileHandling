import csv

# Funkcja do drukowania produktów, które spełniają określone kryteria
def print_filtered_products(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        # Tworzymy obiekt reader do odczytu pliku CSV
        reader = csv.DictReader(file)
        
        # Wydrukuj nagłówek
        print("Filtered Products (Price < 60 and Stock < 40):")
        print("===============================================")
        
        # Iteruj po wierszach i filtruj produkty
        for row in reader:
            # Sprawdzamy, czy cena jest niższa niż 60 i stan magazynowy niższy niż 40
            if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
                # Drukowanie szczegółów produktu
                print(f"Product: {row['Product_Name']}, Price: {row['Price']}, Stock: {row['Stock_Quantity']}")

# Wywołanie funkcji z nazwą pliku
print_filtered_products('clothing.csv')
