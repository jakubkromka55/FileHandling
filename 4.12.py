import csv

# Funkcja do zapisywania książek do pliku w zależności od gatunku
def save_books_by_genre(books, genre, filename):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Genre', 'Year'])  # Nagłówki
        for book in books:
            if book['Genre'] == genre:
                writer.writerow([book['Title'], book['Author'], book['Genre'], book['Year']])

# Funkcja do odczytywania książek z pliku CSV
def read_books_from_csv(file_name):
    books = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Funkcja do filtrowania książek według gatunku i zapisywania do odpowiednich plików
def process_books_by_genre():
    # Wczytanie książek z pliku CSV
    books = read_books_from_csv('books.csv')
    
    # Zapisanie książek do plików w zależności od gatunku
    save_books_by_genre(books, 'Fantasy', 'books_fantasy.txt')
    save_books_by_genre(books, 'Historical', 'books_historical.txt')
    save_books_by_genre(books, 'Romance', 'books_romance.txt')
    save_books_by_genre(books, 'Classic', 'books_classic.txt')

# Uruchomienie programu
process_books_by_genre()
