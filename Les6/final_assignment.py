safes = []
safe_file_path = "kluizen.txt"
for i in range(1, 13):
    safes.append(i)


def menu(show_options):
    if show_options:
        print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
        print("2: Ik wil een nieuwe kluis")
        print("3: Ik wil even iets uit mijn kluis halen")
        print("4: Ik geef mijn kluis terug")
        print("5: Ik wil stoppen")
    choice = 0
    options = ["1", "2", "3", "4", "5"]
    while not valid_choice(choice, options):
        choice = input("Maak een keuze: ")
        if valid_choice(choice, options):
            menu_option = int(choice)
            if menu_option == 1:
                show_available_safes()
            if menu_option == 2:
                new_safe()
            if menu_option == 3:
                open_safe()
            if menu_option == 4:
                remove_safe()
            if menu_option == 5:
                exit()
        else:
            print("Ongeldige optie")


def valid_choice(choice, options):
    return choice in options


def get_available_safes():
    safe_file = open(safe_file_path, "r")
    file_lines = safe_file.readlines()
    safe_file.close()
    return len(safes) - len(file_lines)


def show_available_safes():
    available_safes = get_available_safes()
    print("Er zijn {0} kluizen beschikbaar!".format(available_safes))
    menu(False)


def get_free_safe():
    free_safes = safes
    safe_file = open(safe_file_path, "r")
    file_lines = safe_file.readlines()
    for line in file_lines:
        free_safes.remove(get_safe_number(line))
    safe_file.close()
    return free_safes[0] if len(free_safes) > 0 else 0


def get_safe_number(data):
    return int(data.split(";")[0])


def is_data_correct(number, password):
    is_correct = False
    file = open(safe_file_path, "r")
    file_lines = file.readlines()
    for line in file_lines:
        if get_safe_number(line) == int(number):
            is_correct = password == line.split(";")[1].strip()
            break
    file.close()
    return is_correct


def new_safe():
    if get_available_safes() != 0:
        password = input("Voer een wachtwoord in (minimaal 4 tekens): ")
        if len(password) >= 4:
            safe = get_free_safe()
            if safe != 0:
                file = open(safe_file_path, "a")
                file.write("{0};{1}\n".format(safe, password))
                file.close()
                print("U heeft kluis nummer {0} gekregen!".format(safe))
                menu(True)
            else:
                error("Er zijn momenteel geen kluizen beschikbaar!")
        else:
            error("Ongeldig wachtwoord")
    else:
        error("Er zijn momenteel geen kluizen beschikbaar!")


def open_safe():
    safe_number = input("Voer kluis nummer in: ")
    safe_pass = input("Voer kluis wachtwoord in: ")
    if is_data_correct(safe_number, safe_pass):
        print("Kluis {0} is open!".format(safe_number))
        menu(True)
    else:
        error("Geen kluis gevonden met deze gegevens!")

def get_safe_line(lines, safe_number):
    line_number = 1
    for line in lines:
        if get_safe_number(line) == int(safe_number):
            return line_number
        line_number += 0
    return 0

def remove_safe():
    safe_number = input("Voer kluis nummer in: ")
    safe_pass = input("Voer kluis wachtwoord in: ")
    if is_data_correct(safe_number, safe_pass):
        file = open(safe_file_path, "r+")
        lines = file.readlines()
        safe_line = get_safe_line(lines, safe_number)
        if safe_line > 0:
            del lines[safe_line - 1]
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        file.close()
        menu(True)
    else:
        error("Geen kluis gevonden met deze gegevens!")

def error(msg):
    print(msg)
    input("Druk op enter om terug naar het menu te gaan...")
    menu(True)


menu(True)
