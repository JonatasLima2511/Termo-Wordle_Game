import os
from termo import Termo

os.system("cls" if os.name == "nt" else "clear")

termo = Termo() # Palavra correta

termo.show_grid

print(f"\nTentativas restantes: {termo.MAX_ATTEMPTS - len(termo.attempts)}")
tentativa = str(input("Palavra: ")).upper()
correct = termo.got_it

while termo.can_attempt():
    os.system("cls" if os.name == "nt" else "clear")

    termo.attempt(tentativa)

    correct = termo.got_it

    if not correct and len(termo.attempts) < 6:
        print(f"Tentativas restantes: {termo.MAX_ATTEMPTS - len(termo.attempts)}")
        tentativa = (str(input("Palavra: ")).upper())
    