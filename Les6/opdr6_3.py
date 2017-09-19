def get_sum(number_list):
    total = 0
    for number in number_list:
        total += int(number)
    return total


def get_average(number_list):
    return get_sum(number_list) / len(number_list)


numbers = "5-9-7-1-7-8-3-2-4-8-7-9"
number_list = numbers.split("-")
number_list.sort()
print("Gesorteerde list van ints: {0}".format(number_list))
print("Grootste getal: {0} en Kleinste getal: {1}".format(number_list[0], number_list[len(number_list) - 1]))
print("Aantal getallen: {0} en Som van de getallen: {1}".format(len(number_list), get_sum(number_list)))
print("Gemiddelde: {0}".format(get_average(number_list)))
