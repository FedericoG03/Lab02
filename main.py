import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")

while True:

    t.printMenu()

    txtIn = input()

    # Add input control here!
    if txtIn.isdigit():
        if int(txtIn) == 1:
            print("Ok, quale parola vuoi aggiungere?")
            txtIn = input()
            flag = False
            for parola in txtIn.split(" "):
                if not parola.isalpha():
                    print("Errore, non hai inserito una parola valida!")
                    flag = True
            if flag is False:
                t.handleAdd(txtIn.lower().strip())
                print("Parola aggiunta con successo!")
            pass

        elif int(txtIn) == 2:
            print("Ok, quale traduzione vuoi?")
            txtIn = input()
            flag = False
            for parola in txtIn.split(" "):
                if not parola.isalpha():
                    print("Errore, non hai inserito una parola valida!")
                    flag = True
            if flag is False:
                t.handleTranslate(txtIn.lower().strip())
                print("\nRicerca effetuata con successo!")
            pass
        elif int(txtIn) == 3:
            print("Ok, quale parola devo cercare?")
            txtIn = input()
            if txtIn.count("?") == 1:
                t.handleWildCard(txtIn.lower().strip())
            else:
                print("Formato parola errato!")
            pass

        elif int(txtIn) == 4:
            print("Stampa del dizionario:")
            t.printDictionary()
            pass
        elif int(txtIn) == 5:
            break