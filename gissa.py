from random import randint

nummer = randint(1,10)




while True:
    gissa = int(input("skriv en siffra mellan 1-10 "))
    if gissa == nummer:
        print("Rätt")
        break

    elif gissa > nummer:
        print("för mycket")
    elif gissa < nummer:
        print("för lågt")

    