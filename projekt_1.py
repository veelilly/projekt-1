"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ngoc Khanh Vy Tranová
email: ngtranova@gmail.com
discord: veelilly 
"""
from text_template import TEXTS as texty
   
registrovani_uzivatele = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

uzivatel_heslo = {"bob": "123",
                  "ann": "pass123",
                  "mike": "password123",
                  "liz": "pass123"}

oddelovac = "-" * 40

# Analýza slov:
words = 0
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
sum_numbers = 0
delka_slov = {}

# vyžádá si přihlašovací jméno a heslo 
(username := input("Please insert your username: ")) 
(password := input("Please insert your password: "))
    
# zkontroluje zda jméno a heslo sedí:
if username in uzivatel_heslo and uzivatel_heslo[username] == password:
    # pokud jméno a heslo sedí, pozdraví a pustí ho k analýze 
    print(oddelovac)
    print(f"username: {username}\npassword: {password}")
    print(oddelovac)
    print(f"Welcome to the app, {username} \nWe have 3 texts to be analyzed.")
    print(oddelovac)

    # výběr textu k analýze
    vyber = None    # pomocná proměnná
    while vyber is None:
        vstup = input("Enter a number btw. 1 and 3 to select: ")
        # kontrola jestli je zadané číslo číslo
        if vstup.isdigit():
            cislo = int(vstup) - 1
            if 0 <= cislo < len(texty):
                vyber = cislo
            # pokud číslo není v zadáni
            else:
                print(f" {vstup} is not a valid choice, terminating program..")
                break
        # pokud číslo není číslo        
        else:
            print(f" {vstup} is not a number, terminating program..")
        
    # analýza slov a znaků
        vybrany_text = texty[vyber]
        slova = vybrany_text.split()
        for slovo in slova:
            # vyčistíme každé slovo od čárek a teček
            clean = slovo.strip(",.")
            words += 1
            if clean.istitle() and clean.isalpha():
                titlecase += 1
                print(titlecase)
            if clean.islower():
                lowercase += 1
            if clean.isupper() and clean.isalpha():
                uppercase += 1
            if clean.isnumeric():
                numeric += 1
            if clean.isdigit():
                sum_numbers += int(slovo)
            delka = len(clean)
            if delka in delka_slov:
                delka_slov[delka] += 1
            else:
                delka_slov[delka] = 1 

        # výpis výsledků
        print(oddelovac)
        print(f"There are {words} words in the selected text.")
        print(f"There are {titlecase} titlecase words.")
        print(f"There are {uppercase} uppercase words.")
        print(f"There are {lowercase} lowercase words.")
        print(f"There are {numeric} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers}.")
        print(oddelovac)
        print("LEN|\tOCCURENCES\t|NR.")
        print(oddelovac)

        # sloupcový graf
        for i, pocet in sorted(delka_slov.items()):
            if pocet > 0:
                stars = "*" * pocet
                print(f"{i+1:<3}| {stars:<13}\t|{pocet}")   

# Pokud jmeno a heslo nesedí:
else:
    print(f"username: {username}\npassword: {password}\nuregistered user, terminating the program..")       


    