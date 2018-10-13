from random import sample

print("=" * 40)
print("          SYMULATOR LOTTO")
print("=" * 40)
guessed = False
liczby_gracza = []

while not guessed:

        i = 0
        while i < 6:
            try:
                a = int(input("Podaj liczbę {}: ".format(i+1)))
                if a in liczby_gracza:
                    print("Ta liczba już jest podana!")
                elif a > 0 and a < 50:
                    liczby_gracza.append(int(a))
                    i += 1
                else:
                    raise ValueError
            except ValueError:
                print("To nie jest liczba! Spróbuj ponownie.")
            except TypeError:
                print("To nie jest liczba z zakresu 1- 49! Spróbuj ponownie.")
        liczby_gracza.sort()
        print(liczby_gracza)
        guessed = True


liczby_los = sample(range(1, 50), 6)

print(liczby_los)

if len([i for i in liczby_los if i in liczby_gracza]) >= 3:
    print("Trafiłeś przynajmniej trójkę")
else:
    print("Nie tym razem")