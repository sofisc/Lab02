class Dictionary:
    def __init__(self, dizionario={}):
        self.dizionario=dizionario

    def addWord(self, parola_aliena, traduzione):
        self.dizionario.update({parola_aliena: traduzione})

    def translate(self, aliena):
        tra= self.dizionario[aliena]
        return tra

    def translateWordWildCard(self, parola):
        parola_minuscolo= parola.lower()
        for i in self.dizionario:
            if parola_minuscolo in i:
                return self.dizionario[i]

    def loadDizionario(self, dizionario):
        self.dizionario=dizionario
        print(self.dizionario)