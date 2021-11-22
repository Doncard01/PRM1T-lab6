import sys

def Funkcja1(nazwa):
    file = open(nazwa, 'r')
    wszystkie_znaki = []
    slownik = {}
    nowa_nazwa = str(nazwa)[0:-4] + "_freq.txt"

    for line in file:
        tablica = list(line)
        for i in tablica:
            if i.islower():
                wszystkie_znaki.append(i)

    print(wszystkie_znaki)
    dlugosc = len(wszystkie_znaki)

    for i in wszystkie_znaki:
        ilosc = wszystkie_znaki.count(i)
        czestosc = ilosc/dlugosc
        slownik[i] = czestosc

    print(slownik)

    klucze = list(slownik.keys())
    print(klucze)
    file.close()

    najwiecej = max(slownik.values())

    for key in slownik.keys():
        if slownik[key] == najwiecej:
            return (key, slownik[key])

    with open(nowa_nazwa, "w") as file:
        for keys, values in slownik.items():

            file.write(f"{keys} : {values} \n")


if __name__ == "__main__":
        print(Funkcja1("lorem.txt"))