def names():
    all_names = {}

    result = None
    while result != "":
        result = input("Volgende naam: ")
        if result != "":
            if result in all_names:
                all_names[result] += 1
            else:
                all_names[result] = 1

    for name in all_names:
        if all_names[name] == 1:
            print("Er is 1 student met de naam {0}".format(name))
        else:
            print("Er zijn {0} studenten met de naam {1}".format(all_names[name], name))


names()
