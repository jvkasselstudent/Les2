def convert(celcius):
    return celcius * 1.8 + 32


def table():
    print("{0:>3}\t\t{1:>3}".format("F", "C"))
    for i in range(0, 8):
        celcius = float(-30 + 10 * i)
        print("{0:>5}\t{1:>5}".format(convert(celcius), celcius))


table()
