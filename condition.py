number = 23
running = True

while running:
    guess = int(raw_input('Enter an interger:'))
    if guess==number:
        print "Congooo number matches"
        running = False
    elif guess < number:
        print "No, it lil higher than that"
    else:
        print "No, it is lower than that"

print "Done"
