import time


def add_hardloper(file_path, name):
    file = open(file_path, "a+")
    file.write("{0}, {1}, {2}\n".format(time.strftime("%a %d %b %Y"), time.strftime("%H:%M:%S"), name))
    file.close()


def valid_name(name):
    return name.strip(" ") != ""


name = "placeholder"
while valid_name(name):
    name = input("Naam: ")
    if valid_name(name):
        add_hardloper("hardlopers.txt", name)
