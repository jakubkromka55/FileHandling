import re

# Otwieramy plik z e-mailem
with open('email.txt', 'r', encoding='utf-8') as file:
    email_content = file.read()

# Wzory wyrażeń regularnych
from_pattern = r"From:\s*([^<]+<[^>]+>)"  # Adres nadawcy
to_pattern = r"To:\s*([^<]+<[^>]+>)"  # Adres odbiorcy
subject_pattern = r"Subject:\s*(.*)"  # Temat wiadomości
body_pattern = r"Content-Transfer-Encoding: 7bit\s*(.*)"  # Treść wiadomości

# Szukamy dopasowań za pomocą wyrażeń regularnych
from_match = re.search(from_pattern, email_content)
to_match = re.search(to_pattern, email_content)
subject_match = re.search(subject_pattern, email_content)
body_match = re.search(body_pattern, email_content, re.DOTALL)  # re.DOTALL pozwala na uwzględnienie nowych linii w treści

# Wydobywanie wyników
if from_match:
    sender = from_match.group(1).strip()  # Adres e-mail nadawcy
else:
    sender = "Nie znaleziono nadawcy"

if to_match:
    recipient = to_match.group(1).strip()  # Adres e-mail odbiorcy
else:
    recipient = "Nie znaleziono odbiorcy"

if subject_match:
    subject = subject_match.group(1).strip()  # Temat wiadomości
else:
    subject = "Nie znaleziono tematu"

if body_match:
    body = body_match.group(1).strip()  # Treść wiadomości
else:
    body = "Nie znaleziono treści wiadomości"

# Drukowanie wyników
print("Adres e-mail nadawcy:", sender)
print("Adres e-mail odbiorcy:", recipient)
print("Temat wiadomości:", subject)
print("\nTreść wiadomości:\n", body)
