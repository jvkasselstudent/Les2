result = ""
while len(result) != 4:
    result = input("Geef een string van vier letters: ")
    if len(result) != 4:
        print("{0} heeft {1} letters".format(result, len(result)))
    else:
        break

print("Inlezen van  correcte string: {0} is geslaagd".format(result))
