import dictionary
from dictionary import *

class Translator:

    def __init__(self):
        self.dictionary = {}
        self.diz = Dictionary(dictionary.Dictionary)
        pass

    def printMenu(self):
        print("--------------------------------")
        print("  Traduttore Alieno - italiano  ")
        print("--------------------------------")
        print("1. Aggiungi nuova parola ")
        print("2. Cerca una traduzione ")
        print("3. Cerca una wild card")
        print("4. Stampa tutto il dizionario")
        print("5. Esci")
        print("--------------------------------")
        pass


    def loadDictionary(self, dizionario):
        # dict is a string with the filename of the dictionary
        try:
            #file = open(dict, 'r', encoding='UTF-8')
            for linea in open(dizionario, 'r', encoding='utf-8').readlines():
                try:
                    campi = linea.split(' ')
                    if 3 > len(campi) > 1:
                        self.dictionary[campi[0].lower().strip()] = [campi[1].lower().strip()]
                    elif len(campi) > 2:
                        self.dictionary[campi[0].lower().strip()] = [campi[1].lower().strip()]
                        for i in range(2,len(campi)):
                            self.dictionary[campi[0].lower().strip()].append(campi[i].lower().strip())
                except ValueError:
                    pass
        except FileNotFoundError:
            pass  # Nessun punteggio salvato finora
        self.diz = Dictionary(self.dictionary)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.diz.addWord(entry)
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        self.diz.translate(query)
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        self.diz.translateWordWildCard(query)
        pass
    def printDictionary(self):
        if not self.dictionary:
            print("Il dizionario è vuoto.")
        else:
            for parola, traduzioni in self.dictionary.items():
                print(f"{parola} {' '.join(traduzioni)}")
        pass