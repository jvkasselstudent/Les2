def get_starting_station(stations):
    input_station = ""
    while input_station not in stations:
        input_station = input("Voer een begin station in: ")
        if input_station not in stations:
            print("Station bestaat niet!")
    return input_station


def get_end_station(stations, starting_station):
    input_station = ""
    starting_station_index = stations.index(starting_station)
    end_station_index = -1
    while input_station not in stations and end_station_index < starting_station_index:
        input_station = input("Voer een eind station in: ")
        if input_station not in stations:
            print("Station bestaat niet")
        else:
            if stations.index(input_station) < starting_station_index:
                print("Deze trein komt niet in {0}".format(input_station))
    return input_station


def travel_info(stations, starting_station, end_station):
    rangnummer_start = stations.index(starting_station) + 1
    rangnummer_end = stations.index(end_station) + 1
    distance = rangnummer_end - rangnummer_start

    print("Het beginstation {0} is het {1}e station in het traject.".format(starting_station, rangnummer_start))
    print("Het eindstation {0} is het {1}e station in het traject.".format(end_station, rangnummer_end))
    print("De afstand bedraagt : {0} station(s).".format(distance))
    print("De prijs van het kaartje is {0} euro.".format(distance * 5))
    print("Jij stapt in de trein in: {0}".format(starting_station))
    for station in stations[rangnummer_start:rangnummer_end-1]:
        print("- {0}".format(station))
    print("Jij stapt uit in: {0}".format(end_station))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum, Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']

starting_station = get_starting_station(stations)
end_station = get_end_station(stations, starting_station)
travel_info(stations, starting_station, end_station)
