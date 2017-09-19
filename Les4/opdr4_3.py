def tall_enough(length):
    if length >= 120:
        return "Je bent lang genoeg voor de attractie!"
    else:
        return "Sorry, je bent te klein!"


adultResult = tall_enough(180)
childResult = tall_enough(90)

print(adultResult)
print(childResult)
