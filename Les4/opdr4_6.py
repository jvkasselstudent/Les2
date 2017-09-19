def edit(letters):
    letters.clear()
    letters.extend(["d", "e", "f"])


list = ["a", "b", "c"]
print(list)
edit(list)
print(list)

# Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
# Omdat je de variabel overschrijft met een nieuwe lijst

# Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
# Nee, omdat een string de functies 'clear' & 'extend' niet kent

# Welke rol speelt (im)mutabiliteit in deze vraag?
#