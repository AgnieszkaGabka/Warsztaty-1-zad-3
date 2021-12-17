def zgadnij():
    print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach")

    dobrze = False
    min = 0
    max = 1000
    while not dobrze: #dopóki komputer nie zgdanie liczby gracza, wykonaj poniższe działania
        guess = int((max - min) / 2) + min #oblicznie zgadywanej liczby
        print(f"Zgaduję: {guess}")
        try: #wprowadzenie odpowiedzi przez gracza
            a = (int(input("Wybierz odpowiedź: \
            1 - za dużo\
            2 - za mało\
            3 - zgadłeś")))
            if a == 3:
                print("Wygrałem!")
                dobrze = True
            elif a == 2:
                min = guess #jeśli za mało, przelicz wartość zgadywanej liczby bazując na poprzednio zgadywanej liczbie
            elif a == 1:
                max = guess #jeśli za dużo, przelicz wartość zgadywanej liczby bazując na poprzednio zgadywanej liczbie
            else:
                print("Nie oszukuj!")
        except (ValueError, TypeError):
            print("Wprowadż liczbę!") #jeśli wrowadzona dana nie jest liczbą lub nie mieści się w przedziale 1-1000, wyświetl odpowiedź


print(zgadnij())

