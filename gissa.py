from random import randint

while True:
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

    spela_igen = input("vill du köra igen? (ja/nej): ")
    if spela_igen.lower() == "ja":
        continue
    elif spela_igen.lower() == 'nej':
        print("tack för att du spelade")
        break
