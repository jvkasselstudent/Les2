import xmltodict

file = open("stations.xml", "r")
stations = xmltodict.parse(file.read())["Stations"]["Station"]
print("Dit zijn de codes en types van de 4 stations:")
for station in stations:
    print("{0:4} - {1}".format(station["Code"], station["Type"]))

print()

print("Dit zijn alle stations met één of meer synoniemen:")
for station in stations:
    if station["Synoniemen"] is not None and len(station["Synoniemen"]["Synoniem"]) > 0:
        print("{0:4} - {1}".format(station["Code"], station["Synoniemen"]))

print()
print("Dit is de lange naam van elk station:")
for station in stations:
    print("{0:4} - {1}".format(station["Code"], station["Namen"]["Lang"]))

file.close()