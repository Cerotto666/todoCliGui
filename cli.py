from Modules.Actions import Actions

scelta = -1

while(scelta != Actions.USCITA):
    print()
    print("-" * 20)
    print("1) Crea una nuova lista")
    print("2) Cancella una lista esistente")
    print("3) Modifica una lista esistente")
    print("0) Esci")
    print("-" * 20)
    print()

    try:
        scelta = int(input("Fai la tua scelta"))
    except ValueError:
        print("Input non valido inserisci un numero")

    match scelta:
        case Actions.CREA:
            print("Crea")
        case Actions.CANCELLA:
            print("Cancella")
        case Actions.MODIFICA:
            print("Modifica")
        case _:
            print("Scelta non valida")

print("Programma terminato")



