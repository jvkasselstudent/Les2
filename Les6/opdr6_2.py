def new_list(old_list):
    list = []
    for str in old_list:
        if len(str) == 4:
            list.append(str)
    return list


string_list = eval(input("Geef lijst met minimaal 10 strings: "))

print(new_list(string_list))
