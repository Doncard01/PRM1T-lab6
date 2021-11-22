import csv, sys, os.path

def Funkcja2():
    if len(sys.argv) == 1:
        print("Podaj nazwe pliku w argumencie!")
    else:

        slownik = {}
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], 'r') as file:
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    slownik[row[0]] = row[1]

                print(slownik)

                next_user = "test"
                password = ""

                while next_user != "":
                    next_user = input("Podaj nazwe uzytkownika: ")
                    password = input("Podaj haslo: ")
                    if next_user != "":
                        slownik[next_user] = password

                print(slownik)

                with open(sys.argv[1], "w") as file:
                    writer = csv.writer(file, delimiter=",")
                    for k, v in slownik.items():
                        writer.writerow([k, v])
        else:
            slownik = {}
            next_user = "test"
            password = ""

            while next_user != "":
                next_user = input("Podaj nazwe uzytkownika: ")
                password = input("Podaj haslo: ")
                if next_user != "":
                    slownik[next_user] = password

            print(slownik)

            with open(sys.argv[1], "w") as file:
                writer = csv.writer(file, delimiter=",")
                for k, v in slownik.items():
                    writer.writerow([k, v])



if __name__=="__main__":
    Funkcja2()