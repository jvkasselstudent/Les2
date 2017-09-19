result = ""
numbers = []
while result.strip() != "0":
    result = input("Geef een getal: ")
    if result.isdigit():
        numbers.append(int(result))

print("Er zijn {0} getallen ingevoerd, de som is: {1}".format(len(numbers), sum(numbers)))
