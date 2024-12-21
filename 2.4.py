# Nazwy plików
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Stanowisko
job_title = 'Software Engineer'

# Zapisanie danych wybranych pracowników do pliku
with open(employees_file, 'r') as employees:
    with open(position_file, 'w') as output_file:
        for line in employees:
            if job_title in line:
                output_file.write(line)
