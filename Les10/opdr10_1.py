import xmltodict

file = open("producten.xml", "r")
products = xmltodict.parse(file.read())["artikelen"]["artikel"]
for product in products:
    print(product["naam"])
