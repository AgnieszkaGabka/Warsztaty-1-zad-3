def shot():
    print("Think of a number from 0 to 1000 and I will guess it in max. 10 tries")

    good = False
    min = 0
    max = 1000
    while not good: #dopóki komputer nie zgdanie liczby gracza, wykonaj poniższe działania
        guess = int((max - min) / 2) + min #oblicznie zgadywanej liczby
        print(f"My guess: {guess}")
        try: #wprowadzenie odpowiedzi przez gracza
            a = (int(input("Choose the answer: \
            1 - too big\
            2 - too small\
            3 - you guessed")))
            if a == 3:
                print("I win!")
                good = True
            elif a == 2:
                min = guess #jeśli za mało, przelicz wartość zgadywanej liczby bazując na poprzednio zgadywanej liczbie
            elif a == 1:
                max = guess #jeśli za dużo, przelicz wartość zgadywanej liczby bazując na poprzednio zgadywanej liczbie
            else:
                print("Do not cheatj!")
        except (ValueError, TypeError):
            print("Enter a correct number!") #jeśli wrowadzona dana nie jest liczbą lub nie mieści się w przedziale 1-1000, wyświetl odpowiedź


print(shot())

