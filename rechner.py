def rechner():
    print("Einfacher Rechner")
    zahl = float(input("Gib die erste Zahl ein: "))
    operator = input("Gib den Operator ein (+, -, *, /): ")
    zahl2 = float(input("Gib die zweite Zahl ein: "))

    if operator == "+":
        print(f"Ergebnis: {zahl1 + zahl2}")
    elif operator == "-":
        print(f"Ergebnis: {zahl1 - zahl2}")
    elif operator == "*": 
        print(f"Ergenbis: {zahl1 * zahl2}")
    elif operator == "/":
        if zahl2 != 0:
            print(f"Ergebnis: {zahl1 / zahl2}")
        else:
            print("Man kann nicht durch null teilen!")
    else:
        print("Ungültige Operator!")

    rechner()

        