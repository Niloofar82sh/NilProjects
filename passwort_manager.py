import random
import string
from unicodedata import name
from cryptography.fernet import Fernet
import os

# Dateinamen
SCHLUESSEL_DATEI = "schluessel.key"
PASSWORT_DATEI = "passwoerter.enc"

# Zähler für Aktionen
passwoerter_erstellt = 0
passwoerter_angezeigt = 0

# Schlüssel generieren und speichern
def schluessel_generieren():
    schluessel = Fernet.generate_key()
    with open(SCHLUESSEL_DATEI, "wb") as datei:
        datei.write(schluessel)

# Schlüssel laden
def schluessel_laden():
    return open(SCHLUESSEL_DATEI, "rb").read()

# Passwort generieren
def passwort_generieren(laenge=12):
    zeichen = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(zeichen) for i in range(laenge))

# Passwort speichern
def passwort_speichern(name, passwort, fernet):
    data = f"{name}: {passwort}\n"
    verschluesselte_daten = fernet.encrypt(data.encode())
    with open(PASSWORT_DATEI, "ab") as datei:
        datei.write(verschluesselte_daten)

# Passwörter anzeigen
def passwoerter_anzeigen(fernet):
    if not os.path.exists(PASSWORT_DATEI):
        print("Keine gespeicherten Passwörter vorhanden.")
        return

    print("\n\033[1;32mGespeicherte Passwörter:\033[0m")
    with open(PASSWORT_DATEI, "rb") as datei:
        for zeile in datei:
            entschluesselte_daten = fernet.decrypt(zeile).decode()
            print(entschluesselte_daten.strip())

# Hauptmenü
def hauptmenue():
    global passwoerter_erstellt, passwoerter_angezeigt

    if not os.path.exists(SCHLUESSEL_DATEI):
        schluessel_generieren()
        print("Schlüssel wurde generiert und gespeichert!")

    schluessel = schluessel_laden()
    fernet = Fernet(schluessel)

    while True:
        print("\n\033[1;34mPasswort-Manager\033[0m")
        print("1. Neues Passwort erstellen")
        print("2. Gespeicherte Passwörter anzeigen")
        print("3. Programm beenden")

        auswahl = input("Wählen Sie eine Option: ")

        if auswahl == "1":
            name = input("Name des Kontos/Services: ")
            passwort = passwort_generieren()
            print(f"Generiertes Passwort: {passwort}")
            passwort_speichern(name, passwort, fernet)
            passwoerter_erstellt += 1
        elif auswahl == "2":
            passwoerter_anzeigen(fernet)
            passwoerter_angezeigt += 1
        elif auswahl == "3":
            print(f"\n\033[1;32mZusammenfassung der Aktionen:\033[0m")
            print(f"Anzahl der erstellten Passwörter: {passwoerter_erstellt}")
            print(f"Anzahl der angezeigten Passwörter: {passwoerter_angezeigt}")
            print("\nProgramm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte versuchen Sie es erneut.")
if __name__ == "__main__":
    hauptmenue()