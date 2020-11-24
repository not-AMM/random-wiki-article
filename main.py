import wikipedia
import pyperclip
import webbrowser
# Works in spanish. Will work in an english version
def gen():
    wikipedia.set_lang("es")
    wiki = wikipedia.random(1)
    wpage = wikipedia.page(wiki)
    summ = wikipedia.summary(wiki)
    print("\nSummary:\n--------\n" + summ)
    user = input("¿Quieres leer este tema?: (y/n//ref/q)")
    if user == "no" or user == "n" or user == "N" or user == "No":
            gen()
    elif user == "si" or user == "y" or user == "s" or user == "Si":
        open = input("¿Abrir en el naevagodor o copiar link?: (open/copy)")
        if open == "open" or open == "abrir" or open == "o":
            webbrowser.open(wpage.url,new=2)
        elif open == "copy" or open == "c" or open == "Copy":
            pyperclip.copy(wiki)
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

