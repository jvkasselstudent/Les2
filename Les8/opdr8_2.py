import random


def throw_dice():
    throw_count = 0
    dice1 = dice2 = 0
    while dice1 == dice2 and throw_count < 3:
        throw_state = ""
        throw_count += 1
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            if throw_count != 3:
                throw_state = "(dubbel)"
            else:
                throw_state = "(direct naar gevangenis)"
        print("{0} + {1} = {2} {3}".format(dice1, dice2, dice1 + dice2, throw_state))


throw_dice()
