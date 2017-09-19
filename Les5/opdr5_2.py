def print_kaartnummers(file_path):
    file = open(file_path, "rt")
    file_lines = file.readlines()
    for line in file_lines:
        line_data = line.strip().split(",")
        kaart_gegevens = get_kaart_gegevens(line_data)
        print("{0} heeft kaartnummer: {1}".format(kaart_gegevens[0], kaart_gegevens[1]))
    file.close()


def get_kaart_gegevens(kaart_data):
    kaartnummer = int(kaart_data[0])
    naam = kaart_data[1][1:] if kaart_data[1][0] == " " else kaart_data[1]
    return [naam, kaartnummer]


print_kaartnummers("kaartnummers.txt")
