import os
import pickle
import language
import college
import item
import adventureskill
import talent
import spell
import transformation
import character
import raceability
import formula
import rankingchoice

global selectedChar

allStats = [
    "ps", "md", "ag",
    "ma", "wp", "en",
    "ft", "pc", "tmr",
    "ht", "wt", "pb",
    "ep"
    ]


def myInput():
    '''handle the input of the main menu, split via spaces'''
    com = input("> ").split(" ")
    if(com[0] == "save" and len(com) == 1):
        doSaveChar()
        myInput()
    elif(com[0] == "new" and len(com) == 1):
        doNewChar()
        myInput()
    elif(com[0] == "random" and len(com) == 1):
        doNewRandChar("")
        myInput()
    elif(com[0] == "random" and len(com) == 2):
        doNewRandChar(com[1])
        myInput()
    elif(com[0] == "get" and len(com) == 2):
        getStat(com[1])
        myInput()
    elif(com[0] in allStats and len(com) == 1):
        getStat(com[0])
        myInput()
    elif(com[0] == "set" and len(com) == 3):
        setStat(com[1], com[2])
        myInput()
    elif(com[0] in allStats and len(com) == 2):
        if("+" in com[1]):
            modStat(com[0], com[1])
            myInput()
        elif("-" in com[1]):
            modStat(com[0], com[1])
            myInput()
        else:
            setStat(com[0], com[1])
            myInput()
    elif(com[0] == "?" and len(com) == 1):
        help()
        myInput()
    elif(com[0] == "view" and len(com) == 1):
        showStats()
        myInput()
    elif(com[0] == "ranking" and len(com) == 1):
        ranking_menu()
        myInput()
    elif(com[0] == "q" and len(com) == 1):
        doSaveChar()
        exit()
    elif(com[0] == None or com[0] == ""):
        myInput()
    else:
        print("command not recognised, type ? for help")
        myInput()


def menu():
    os.system('cls')
    tryLoadChar()
    print("Speedy's Digital DQ sheet")
    print("--------------------------------")
    print("Type ? for help and q to quit")
    #print("DEBUG---------------------------")
    #print(selectedChar.getRAbilities())
    myInput()

def ranking_menu():
    os.system('cls')
    print("DQ Ranking Menu - " + selectedChar.getName())
    print("--------------------------------")
    print("Your EP is: " + str(selectedChar.getEP()))
    print("Your SP is: " + str(selectedChar.getSP()))
    print("Adventure Time to spend is unknown")
    print("")
    print("to start ranking, type: 'start'")
    print("to stop ranking, type: 'stop'")
    print("to view ranking, type: 'view'")
    print("to add a single new entry, type: 'add'")
    print("to leave this menu, type: 'q'")
    print("--------------------------------")
    ranking_input()
    
def ranking_input():
    com = input("> ").split(" ")
    if(com[0] == "start" and len(com) == 1):
        ranking_control(True)
        ranking_input()
    elif(com[0] == "stop" and len(com) == 1):
        ranking_control(False)
        ranking_input()
    elif(com[0] == "add" and len(com) == 1):
        ranking_add()
        ranking_input()
    elif(com[0] == "view" and len(com) == 1):
        ranking_view()
        ranking_input()
    elif(com[0] == "delete" and len(com) == 1):
        ranking_remove(int(input("enter a #: > ")))
        ranking_input()   
    elif(com[0] == "delete" and len(com) == 2):
        ranking_remove(com[1])
        ranking_input()    
    elif(com[0] == "q" and len(com) == 1):
        doSaveChar()
        menu()
    else:
       ranking_input()

def ranking_control(begin):
    while(begin):
        ranking_add()
    
def ranking_add():
    print("--------------------------------")
    name = input("Name: > ")
    if name == "q":
        ranking_control(False)
    ep = input("EP Cost: > ")
    sp = input("SP Cost: > ")
    time = input("Time Cost (days): > ")
    prev = input("Previous Rank: > ")
    curr = input("Current Rank: > ")
    print("Adding: " + name)
    thing = rankingchoice.RankingChoice(name, ep, sp, time, prev, curr)
    selectedChar.rankinglog.append(thing)
    #print(selectedChar.rankinglog)
    ranking_input()

def ranking_remove(index):
    print("Removing "+ selectedChar.rankinglog[int(index)] +"...")
    try:
        selectedChar.rankinglog.pop(int(index))
        print("Done!")
    except:
        print("Error deleting "+ selectedChar.rankinglog[int(index)])

def ranking_view():
    print("NAME \t\t| EP \t\t| SP \t\t| TIME \t\t| P. RANK \t\t| C. RANK")
    print("------------------------------------------------------------------------------------------------")
    i = 0
    for x in selectedChar.rankinglog:
        try:
            print(str(i) + ")" + x.getname() + " \t\t\t| " +  x.getepcost() + " \t\t| " + x.getspcost() + " \t\t| " + x.gettimecost()+ " \t\t| " + x.getprev() + " \t\t| " + x.getcurrent())
        except:
            print(str(i) + ")" +x.getname() + " has an error")
        
        i = i + 1
    
    # add things to calculate
    # - name
    # - ep cost
    # - sp cost
    # - time cost

    # calculate

def tryLoadChar():
    global selectedChar
    try:
        print("Trying to import existing char...")
        with open('char.file', 'rb') as Char:
            myChar = pickle.load(Char)
            Char.close()
            selectedChar = myChar
            if(myChar == None):
                print("No character found...")
            else:
                print(myChar.getName() + " the " + myChar.getLevel())
            print("Done!")
        print("--------------------------------")
    except:
        print("No char.file, generating...")
        with open('char.file', 'w') as fp:
            fp.close()


def doLoadChar():
    global selectedChar
    print("List of your characters:")
    #with open


def doNewChar():
    global selectedChar
    print("New character sheet! wooo!")
    player = character.Character(input("Name: "))
    player.create()
    selectedChar = player
    doSaveChar()
    print("ALL DONE!")
    print("--------------------------------")


def doNewRandChar(name):
    global selectedChar
    print("Generating a new random bunny character!")
    player = character.Character(name)
    print("Generating...")
    player.createRandom(name)
    selectedChar = player
    doSaveChar()
    print("ALL DONE!")
    print("--------------------------------")
    showStats()


def doSaveChar():
    global selectedChar
    print("Saving your data, please wait...")
    with open('char.file', 'wb') as Char:
        pickle.dump(selectedChar, Char)
        Char.close()
    print("Done! :)")
    print("--------------------------------")


def getStat(stat):
    global selectedChar
    if(stat.lower() in allStats):
        if(stat.lower() == "ps"):
            print(selectedChar.getPS())
        elif(stat.lower() == "md"):
            print(selectedChar.getMD())
        elif(stat.lower() == "ag"):
            print(selectedChar.getAG())
        elif(stat.lower() == "ma"):
            print(selectedChar.getMA())
        elif(stat.lower() == "wp"):
            print(selectedChar.getWP())
        elif(stat.lower() == "en"):
            print(selectedChar.getEN())
        elif(stat.lower() == "ft"):
            print(selectedChar.getFT())
        elif(stat.lower() == "pc"):
            print(selectedChar.getPC())
        elif(stat.lower() == "tmr"):
            print(selectedChar.getTMR())
        elif(stat.lower() == "ht"):
            print(selectedChar.getHeight())
        elif(stat.lower() == "wt"):
            print(selectedChar.getWeight())
        elif(stat.lower() == "pb"):
            print(selectedChar.getBeauty())
        elif(stat.lower() == "ep"):
            print(selectedChar.getEP())
        elif(stat.lower() == "advep"):
            print(selectedChar.advep)

    else:
        print("Selectable stats are:")
        print(*allStats, sep=", ")


def setStat(stat, value):
    global selectedChar
    if(stat.lower() in allStats and value != None):
        if(stat.lower() == "ps"):
            selectedChar.setPS(value)
            print("Set to: " + str(selectedChar.getPS()))
        elif(stat.lower() == "md"):
            selectedChar.setMD(value)
            print("Set to: " + str(selectedChar.getMD()))
        elif(stat.lower() == "ag"):
            selectedChar.setAG(value)
            print("Set to: " + str(selectedChar.getAG()))
        elif(stat.lower() == "ma"):
            selectedChar.setMA(value)
            print("Set to: " + str(selectedChar.getMA()))
        elif(stat.lower() == "wp"):
            selectedChar.setWP(value)
            print("Set to: " + str(selectedChar.getWP()))
        elif(stat.lower() == "en"):
            selectedChar.setEN(value)
            print("Set to: " + str(selectedChar.getEN()))
        elif(stat.lower() == "ft"):
            selectedChar.setFT(value)
            print("Set to: " + str(selectedChar.getFT()))
        elif(stat.lower() == "pc"):
            selectedChar.setPC(value)
            print("Set to: " + str(selectedChar.getPC()))
        elif(stat.lower() == "tmr"):
            selectedChar.setTMR(value)
            print("Set to: " + str(selectedChar.getTMR()))
        elif(stat.lower() == "ht"):
            selectedChar.setHeight(value)
            print("Set to: " + str(selectedChar.getHeight()))
        elif(stat.lower() == "wt"):
            selectedChar.setWeight(value)
            print("Set to: " + str(selectedChar.getWeight()))
        elif(stat.lower() == "pb"):
            selectedChar.setBeauty(value)
            print("Set to: " + str(selectedChar.getBeauty()))
        #----------------------------------------------------
        elif(stat.lower() == "ep"):
            selectedChar.setEP(value)
            print("Set to: " + str(selectedChar.getEP()))
    else:
        print("Incorrect stat or value, please use the following:")
        print(*allStats, sep=", ")


def modStat(stat, value):
    global selectedChar
    value = int(value)
    if(stat.lower() in allStats and value != None):
        if(stat.lower() == "ps"):
            oldValue = selectedChar.getPS()
            newValue = oldValue + value
            selectedChar.setPS(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getPS()))
        elif(stat.lower() == "md"):
            oldValue = selectedChar.getMD()
            newValue = oldValue + value
            selectedChar.setMD(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getMD()))
        elif(stat.lower() == "ag"):
            oldValue = selectedChar.getAG()
            newValue = oldValue + value
            selectedChar.setAG(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getAG()))
        elif(stat.lower() == "ma"):
            oldValue = selectedChar.getMA()
            newValue = oldValue + value
            selectedChar.setMA(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getMA()))
        elif(stat.lower() == "wp"):
            oldValue = selectedChar.getWP()
            newValue = oldValue + value
            selectedChar.setWP(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getWP()))
        elif(stat.lower() == "en"):
            oldValue = selectedChar.getEN()
            newValue = oldValue + value
            selectedChar.setEN(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getEN()))
        elif(stat.lower() == "ft"):
            oldValue = selectedChar.getFT()
            newValue = oldValue + value
            selectedChar.setFT(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getFT()))
        elif(stat.lower() == "pc"):
            oldValue = selectedChar.getPC()
            newValue = oldValue + value
            selectedChar.setPC(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getPC()))
        elif(stat.lower() == "tmr"):
            oldValue = selectedChar.getTMR()
            newValue = oldValue + value
            selectedChar.setTMR(newValue)
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getTMR()))
        #----------------------------------------------------
        elif(stat.lower() == "ep"):
            oldValue = selectedChar.ep
            newValue = oldValue + value
            selectedChar.ep = newValue
            print("Updated from: " + str(oldValue)
                  + " to: " + str(selectedChar.getEP()))
    else:
        print("Incorrect stat or value, please use the following:")
        print(*allStats, sep=", ")


def getRacialAbilities():
    print("Racial abilities:")
    for rab in selectedChar.rabilities:
        print(rab.getDesc() + "\n")


def showStats():
    os.system("CLS")
    print("Name: " + str(selectedChar.getName()))
    print("Race: " + str(selectedChar.getRace()))
    print("Level: " + str(selectedChar.getLevel()))
    print("Height: " + str(selectedChar.getHeight()))
    print("Weight: " + str(selectedChar.getWeight()))
    print("PB: " + str(selectedChar.getBeauty()))
    print("Age: " + str(selectedChar.getAge()))
    print("Sex: " + str(selectedChar.getSex()))
    print("Hand: " + str(selectedChar.getHand()))
    print("Aspect: " + str(selectedChar.getAspect()))
    print("Social Status: " + str(selectedChar.getSocial()))
    print("Birth: " + str(selectedChar.getBirth()))
    print("--------------------------------")
    print("PS: " + str(selectedChar.getPS()))
    print("MD: " + str(selectedChar.getMD()))
    print("AG: " + str(selectedChar.getAG()))
    print("MA: " + str(selectedChar.getMA()))
    print("WP: " + str(selectedChar.getWP()))
    print("EN: " + str(selectedChar.getEN()))
    print("FT: " + str(selectedChar.getFT()))
    print("PC: " + str(selectedChar.getPC()))
    print("TMR: " + str(selectedChar.getTMR()))
    print("EP Mod: " + str(selectedChar.getEPMod()))
    print("Natural Armour: " + str(selectedChar.getNaturalArmour()))
    print("--------------------------------")
    getRacialAbilities()
    print("--------------------------------")
    print("EP Remaining: " + str(selectedChar.ep))
    print("Adventure Skill EP Remaining: " + str(selectedChar.advep))
    print("--------------------------------")
    myInput()


def help():
    os.system("CLS")
    print("Help Menu")
    print("--------------------------------")
    print("[1.] new - generate a new char sheet")
    print("[2.] load - load an existing char sheet")
    print("[3.] random [name]- generate a new random char sheet")
    print("[4.] save - save your current char sheet")
    print("[5.] get [stat] - displays your current stat value")
    print("[6.] [stat] - same as 'get [stat]'")
    print("[7.] view - view a full list of all stats")
    print("[8.] set [stat] value - replaces old value with new value")
    print("[9.] [stat] [[+ or -]value] - modify an existing value")
    print("[10.]")
    print("[11.]")
    print("[12.]")
    print("[13.]")


menu()
