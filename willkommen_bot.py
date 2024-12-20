# Willkommen-Bot
# Ein einfacher Python-Skript für eine Begrüßung auf Deutsch.

from os import name


def willkommen_bot():
    print("Willkommen! Bitte geben Sie Ihren Namen ein:")
    name = input("Name: ")
    print(f"Hallo {name}! Schön, dich zu sehen!")
    print("Möchten Sie weitere Informationen? (ja/nein)")

    antwort = input("Antwort: ").strip().lower()
    if antwort == "ja":
        print("Wir freuen uns, dass Sie hier sind! Viel Spaß beim Programmieren!")
    elif antwort == "nein":
        print("Kein Problem! Hab einen schönen Tag!")
    else:
        print("Entschuldigung, ich habe Sie nicht verstanden. Bitte versuchen Sie es erneut!")

if __name__ == "__main__":
    willkommen_bot()
