class Dictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def addWord(self, entry):
        parola = entry.split(" ")[0]
        traduzioni = entry.split(" ")[1:]
        if parola in self.dictionary:
            for trad in traduzioni:
                if trad not in self.dictionary[parola]:
                    self.dictionary[parola].append(trad)
        else:
            self.dictionary[parola] = traduzioni
        with open("dictionary.txt", "w") as file:
            for chiave, valori in self.dictionary.items():
                file.write(f"{chiave} {' '.join(valori)}\n")

    def translate(self,query):
        mystr = ""
        if query not in self.dictionary:
            mystr = "Parola non presente nel dizzionario."
        else:
            for traduzione in self.dictionary[query]:
                mystr += traduzione + "\n"
        print(mystr)

    def translateWordWildCard(self,query):
        x = query.find("?")
        mystr = ""

        for parola in self.dictionary.keys():
            if parola[:x] == query[:x] and parola[x+1:] == query[x+1:]:
                for traduzione in self.dictionary[parola]:
                    mystr += traduzione + "\n"
        print(mystr)