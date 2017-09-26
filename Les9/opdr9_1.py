hotel_costs = 4356

try:
    person_count = int(input("Hoeveel personen gaan er mee? "))
    costs_per_person = hotel_costs / person_count
    print("De kosten per persoon zijn {0}".format(costs_per_person))
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except BaseException:
    print("Onjuiste invoer!")
