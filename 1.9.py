###
# Prints employees employed in a specified position.
###

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

# Otwórz plik i przetwarzaj linie
with open(file_name) as file:
    header = next(file)  # Pomijamy nagłówek
    count = 1
    for line in file:
        if job_title in line:
            print(f"{count}. {line.strip()}")
            count += 1
