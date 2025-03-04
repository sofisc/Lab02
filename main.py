import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere? ")
        txtIn = input()
        t.handleAdd(txtIn)
        print("Aggiunta!")
    elif int(txtIn) == 2:
        print("Ok, quale traduzione devo cercare? ")
        txtIn = input()
        t.handleTranslate(txtIn)
    elif int(txtIn) == 3:
        print("Ok, quale parola devo cercare? ")
        txtIn = input()
        t.handleWildCard(txtIn)
    elif int(txtIn) == 4:
        break