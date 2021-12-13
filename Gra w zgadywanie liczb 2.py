def zgadnij():
    print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach")

    dobrze = False
    min = 0
    max = 1000
    while not dobrze:
        guess = int((max - min) / 2) + min
        print(f"Zgaduję: {guess}")
        try:
            a = (int(input("Wybierz odpowiedź: \
            1 - za dużo\
            2 - za mało\
            3 - zgadłeś")))
            if a == 3:
                print("Wygrałem!")
                dobrze = True
            elif a == 2:
                min = guess
            elif a == 1:
                max = guess
            else:
                print("Nie oszukuj!")
        except (ValueError):
            print("Wprowadż liczbę!")


print(zgadnij())