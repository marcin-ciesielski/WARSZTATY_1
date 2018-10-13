from random import randint

print("="*42)
print("Gra w zgadywanie liczb w zakresie 0-100.")
print("=" * 42)

guessed = False
rnd = randint(1, 100)

while not guessed:
    try:
        str_num = input("Zgadnij liczbę: ")
        num = int(str_num)
        if num == rnd:
            print("Zgadłeś!")
            guessed = True
        elif num < rnd:
            print("Za mało!")
        else:
            print("Za dużo!")
    except ValueError:
            print("To nie jest liczba! Spróbuj ponownie.")
