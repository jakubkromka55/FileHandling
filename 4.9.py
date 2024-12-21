import csv

# Funkcja do drukowania danych osób zatrudnionych na stanowisku 'Graphic Designer'
def print_graphic_designers(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        # Tworzymy obiekt reader do odczytu pliku CSV
        reader = csv.DictReader(file)
        
        # Wydrukuj nagłówek
        print("GRAPHIC DESIGNERS")
        print("=================")
        
        # Iteruj po wierszach i filtruj osoby na stanowisku 'Graphic Designer'
        for row in reader:
            if row['Job Title'] == 'Graphic Designer':
                # Drukowanie imienia, nazwiska oraz e-maila
                print(f"{row['First Name']} {row['Last Name']},{row['Email']}")

# Wywołanie funkcji z nazwą pliku
print_graphic_designers('it_company.csv')
