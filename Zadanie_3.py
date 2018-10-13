from random import randint

print("=" * 40)
print("    Gra w zgadywanie liczb wersja 2")
print("=" * 40)

print("Pomyśl sobie liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach\n")
min = 0
max = 1000
count = 0
koniec = False
guess = int((max - min) / 2) + min
while count < 10:
    try:
        print("Zgaduję : {}\n".format(guess))
        print("Wybierz: za dużo (1), za mało (2), zgadłeś (3)")
        result = input("Twoja odpowiedź: ")
        if int(result) == 3:
            print("Wygrałeś")
            count = 10
        elif int(result) == 1:
            max = guess
        elif int(result) == 2:
            min = guess
        else:
            raise ValueError
    except ValueError:
        print("To nie jest poprawna odpowiedź!")
    guess = int((max - min) / 2) + min
    count += 1
