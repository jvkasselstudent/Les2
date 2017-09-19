def average(text):
    words = text.split(" ")
    chars = 0
    for word in words:
        chars += len(word)
    average_chars = chars / len(words)
    print("Gemiddelde lengte is: {0}".format(average_chars))


text = input("Typ een zin: ")
average(text)
