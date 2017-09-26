import datetime
import csv

file_path = 'inloggers.csv'

file = open(file_path, "a+")

surname = ""
while surname != "einde":
    surname = input("Wat is je achternaam? ")
    if surname == "einde":
        break
    initials = input("Wat zijn je voorletters? ")
    date_of_birth = datetime.datetime.strptime(input("Wat is je geboortedatum? "), "%d-%m-%Y").date()
    email = input("Wat is je e-mail adres? ")
    current_date = datetime.datetime.now().strftime("%a %d %b %Y at %H:%M")
    csv_writer = csv.writer(file, delimiter=' ', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([current_date, initials, surname, date_of_birth, email])
file.close()
