
äpplen = 7
päron = 13


while True:
    antal_äpplen = int(input("hur många äpplen såldes?"))
    antal_päron = int(input("hur många päron såldes?"))

    äpplen_pengar = äpplen * antal_äpplen
    päron_pengar = päron * antal_päron

    if äpplen_pengar < päron_pengar:
        print(f"axel sålde äpplen för", [päron_pengar])
    if äpplen_pengar > päron_pengar:
        print("Petra sålde äpplen för",[äpplen_pengar])
    elif äpplen_pengar == päron_pengar:
        print("Dem sålde för lika mycket")

