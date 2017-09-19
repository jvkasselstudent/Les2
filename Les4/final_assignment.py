def default_price(distance):
    if distance < 0:
        return 0
    if distance < 50:
        return distance * 0.8
    else:
        return 15 + distance * 0.6


def ticket_price(age, weekend_ticket, distance):
    price = default_price(distance)
    if age < 12 or age >= 65:
        discount = 35 if weekend_ticket else 30
    else:
        discount = 40 if weekend_ticket else 0
    price -= price / 100 * discount
    return format_price(price)


def format_price(price):
    return "{0:.2f}".format(price)


def test_expectation(expectation, age, weekend_ticket, distance):
    print("Expecting {0} got {1}".format(format_price(expectation), ticket_price(age, weekend_ticket, distance)))
    return format_price(expectation) == ticket_price(age, weekend_ticket, distance)


def do_tests():
    ages = [11, 12, 64, 65]
    distances = [-30, 20, 70]
    expectations = [0.00, 11.20, 39.90, 0.00, 10.40, 37.05, 0.00, 16.00, 57.00, 0.00, 9.60, 34.20, 0.00, 16.00, 57.00,
                    0.00, 9.60, 34.20, 0.00, 11.20, 39.90, 0.00, 10.40, 37.05]
    i = 0
    for age in ages:
        for is_weekend in range(0, 2):
            for distance in distances:
                success = test_expectation(expectations[i], age, bool(is_weekend), distance);
                if success:
                    print("Test succeed")
                else:
                    print("Test failed")
                i += 1


do_tests()
