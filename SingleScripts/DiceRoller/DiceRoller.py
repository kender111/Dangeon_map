from random import randint

while True:
    diceNumber = input('Choose number of dices ')
    diceType = input('Choose dice type ')
    dice = 0
    diceTotal = 0

    for dice in range(0, int(diceNumber)):
        diceRoll = randint(1, int(diceType))
        diceTotal = diceTotal + diceRoll
        print("Dice #%r = %r" % (dice+1, diceRoll))
    print("Result is %r" % diceTotal)
