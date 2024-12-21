import re

# Pobierz nazwę użytkownika i hasło z klawiatury
username = input("Enter username: ")
password = input("Enter password: ")

# Wzór wyrażenia regularnego dla nazwy użytkownika
username_pattern = r'^[a-z]{6,}$'  # co najmniej 6 małych liter

# Wzór wyrażenia regularnego dla hasła
password_pattern = r'^[A-Za-z0-9_]{8,}$'  # co najmniej 8 znaków, litery, cyfry, podkreślenie

# Sprawdzenie, czy nazwa użytkownika pasuje do wzorca
username_match = re.match(username_pattern, username)

# Sprawdzenie, czy hasło pasuje do wzorca
password_match = re.match(password_pattern, password)

# Wynik
if username_match and password_match:
    print("Username and password are valid.")
else:
    print("Invalid username or password.")
