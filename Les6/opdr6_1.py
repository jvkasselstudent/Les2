def get_season(month):
    seasons = {
        "Lente": [3, 4, 5],
        "Zomer": [6, 7, 8],
        "Herfst": [9, 10, 11],
        "Winter": [1, 2, 12]
    }
    for season in seasons:
        if month in seasons[season]:
            return season


for i in range(1, 13):
    print("Maand {0} hoort bij seizoen {1}".format(i, get_season(i)))
