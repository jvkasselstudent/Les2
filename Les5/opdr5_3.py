def get_grootste_kaartnummer(file_path):
    file = open(file_path, "r")
    file_lines = file.readlines()
    data = [0, 0, len(file_lines)]
    line_number = 1
    for line in file_lines:
        line_data = line.strip().split(",")
        kaartnummer = int(line_data[0])
        if kaartnummer > data[0]:
            data[0] = kaartnummer
            data[1] = line_number
        line_number += 1
    file.close()
    return data


gegevens = get_grootste_kaartnummer("kaartnummers.txt")

print("Deze file telt {0} regels".format(gegevens[2]))
print("Het grootste kaartnummer is: {0} en dat staat op regel {1}".format(gegevens[0], gegevens[1]))
