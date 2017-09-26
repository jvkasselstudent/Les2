import csv


def write_file(file_path, headers, rows):
    file = open(file_path, "w")
    writer = csv.DictWriter(file, headers, delimiter=';', quotechar=' ')

    writer.writeheader()
    writer.writerows(rows)
    file.close()


def get_products_from_file(file_path):
    products = []
    file = open(file_path, "r")
    reader = csv.DictReader(file, delimiter=';', quotechar=' ')
    for row in reader:
        products.append(row)
    file.close()
    return products


def create_items(keys, content):
    items = []
    for item in content:
        dictionary = dict.fromkeys(keys)
        for key_index in range(len(keys)):
            dictionary.update({keys[key_index]: item[key_index]})
        items.append(dictionary)
    return items


def create_products(file_path, headers):
    content = [
        [121, "ABC123", "Highlight pen", 231, 0.56],
        [123, "PQR678", "Nietmachine", 587, 9.99],
        [128, "ZYX163", "Bureaulamp", 34, 19.95],
        [137, "MLK709", "Monitorstandaard", 66, 32.50],
        [271, "TRS665", "Ipad hoes", 155, 19.01]
    ]

    items = create_items(headers, content)

    write_file(file_path, headers, items)


def get_most_expensive_product(products, priceKey):
    most_expensive_product = None
    for product in products:
        if most_expensive_product is None or float(product[priceKey]) > float(most_expensive_product[priceKey]):
            most_expensive_product = product
    return most_expensive_product


def get_product_by_item(products, header, value):
    for product in products:
        if product[header] == value:
            return product
    return None


def get_total_product_count(products):
    product_count = 0
    for product in products:
        product_count += int(product["Voorraad"])
    return product_count


products_file = "producten.csv"
headers = ["Artikelnummer", "Artikelcode", "Naam", "Voorraad", "Prijs"]

create_products(products_file, headers)
products = get_products_from_file(products_file)

most_expensive_product = get_most_expensive_product(products, "Prijs")
print("Het duurste artikel is {0} en die kost {1} Euro".format(most_expensive_product["Naam"],
                                                               most_expensive_product["Prijs"]))

product_bureaulamp = get_product_by_item(products, "Artikelnummer", "128")
print("Er zijn slechts {0} exemplaren in voorraad van het product met nummer {1}".format(product_bureaulamp["Voorraad"], product_bureaulamp["Artikelnummer"]))

print("In totaal hebben wij {0} producten in ons magazijn liggen".format(get_total_product_count(products)))
