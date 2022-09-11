import pickle

with open('char.file', 'rb') as Char:
    myChar = pickle.load(Char)
    Char.close()
    print(myChar.getName())
