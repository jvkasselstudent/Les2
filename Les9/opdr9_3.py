import csv

file = open('gamers.csv', "r")
reader = csv.reader(file, delimiter=';', quotechar=' ')
highscore_player = None
for gamer in reader:
    if highscore_player == None:
        highscore_player = gamer
    else:
        if gamer[2] > highscore_player[2]:
            highscore_player = gamer
print("De hoogste score is: {0} op {1} behaald door {2}".format(highscore_player[2], highscore_player[1], highscore_player[0]))

file.close()