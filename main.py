import wikipedia
import pyperclip
import webbrowser

def gen():
    wikipedia.set_lang("es")
    wiki = wikipedia.random(1)
    wpage = wikipedia.page(wiki)
    summ = wikipedia.summary(wiki)
    link = wpage.url
# This is to give format to the results. I will work on a CLI or a minimal GUI
    large = len(wiki)
    division = "+----------" + ("-" * large) + "+"
# The program starts
    print("\nGenerando nueva entrada...\n")
    print(division + "\n| Título: " + wiki + " |\n" + division)
    print("| Resumen:\n+---------\n" + summ + "\n")
    user = input("- ¿Quieres leer este tema?: (y/n/q)\n: ")
# Replace is to avoid errors caused by a blank space
    user = user.replace(" ", "")
    if user == "no" or user == "n" or user == "N" or user == "No":
            gen()
    elif user == "si" or user == "y" or user == "s" or user == "Si":
# You can choose to open the link in your default browser or just copy it into your clipboard
        open = input("- ¿Abrir en el navegador o copiar link?: (open/copy)\n: ")
        open = open.replace(" ", "")
        if open == "open" or open == "abir" or open == "o" or open == "a":
            webbrowser.open(wpage.url,new=2)
        elif open == "copy" or open == "c" or open == "Copy":
            pyperclip.copy(link)
            print("- Título: " + wiki + "\n" + "- Link: " + link)
            gen()
        else:
            gen()
            exit(0)
    elif user == "q" or user == "salir" or user == "quit" or user == "Q" or user == "s":
        exit(0)
    else:
        print("*-Entrada NO aceptada-*")
        gen()

gen()
