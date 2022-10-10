import raceability

import random

raceList = [
    "dwarf", "elf", "halfling",
    "hill giant", "human",
    "orc", "shapechanger"
    ]

aspectList = [
    "winter air", "winter water", "winter earth", "winter fire",
    "spring air", "spring water", "spring earth", "spring fire",
    "summer air", "summer water", "summer earth", "summer fire",
    "autumn air", "autumn water", "autumn earth", "autumn fire",
    "solar", "lunar", "life", "death"
]

socialList = [
    "trash / criminal", "boned",
    "skilled retainer", "goodman",
    "master", "military",
    "gentry", "lesser noble",
    "merchant prince", "greater noble"
]


class Character:
    def __init__(self, name):
        self.level = ""
        self.name = name
        self.rabilities = []  # racial abilities list
        self.adventureskills = []  # adventure skills list
        self.ep = 0
        self.advep = 0

    def getLevel(self):
        return self.level

    #characteristic points------------------------------------------------------
    def getPS(self):
        return self.ps

    def getMD(self):
        return self.md

    def getAG(self):
        return self.ag

    def getMA(self):
        return self.ma

    def getWP(self):
        return self.wp

    def getEN(self):
        return self.en

    def setPS(self, ps):
        self.ps = ps

    def setMD(self, md):
        self.md = md

    def setAG(self, ag):
        self.ag = ag

    def setMA(self, ma):
        self.ma = ma

    def setWP(self, wp):
        self.wp = wp

    def setEN(self, en):
        self.en = en

    #seccondary characteristics-------------------------------------------------
    def getFT(self):
        return self.ft

    def getPC(self):
        return self.pc

    def getTMR(self):
        return self.tmr

    def setFT(self, ft):
        self.ft = ft

    def setPC(self, pc):
        self.pc = pc

    def setTMR(self, tmr):
        self.tmr = tmr

    # race----------------------------------------------------------------------
    def getRace(self):
      return self.race

    def setRace(self, race):
        self.race = race.lower()

    #racial abilities
    def getRAbilities(self):
      return self.rabilities

    def addRAbilities(self, desc):
        self.rabilities.append(raceability.Racialability(desc))

    #racial stats cont.

    def getEPMod(self):
        return self.epmod

    def setEPMod(self, epmod):
        self.epmod = epmod

    def getNaturalArmour(self):
        return self.na

    def setNaturalArmour(self, na):
        self.na = na

    #todo - add extra skills and abilities based on race

    #description----------------------------------------------------------------
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name.lower()

    def getAge(self):
      return self.age

    def setAge(self, age):
        self.age = age

    def getSex(self):
      return self.sex

    def setSex(self, sex):
        self.sex = sex.lower()

    def getHand(self):
      return self.hand

    def setHand(self, hand):
        self.hand = hand.lower()

    def getHeight(self):
      return self.ht

    def setHeight(self, ht):
        self.ht = ht

    def getWeight(self):
      return self.wt

    def setWeight(self, wt):
      self.wt = wt

    def getBeauty(self):
        return self.pb

    def setBeauty(self, pb):
        self.pb = pb

    #aspect---------------------------------------------------------------------
    def getAspect(self):
      return self.aspect

    def setAspect(self, aspect):
        self.aspect = aspect.lower()

    #heritage-------------------------------------------------------------------
    def getSocial(self):
      return self.social

    def setSocial(self, social):
        self.social = social.lower()

    def getBirth(self):
      return self.birth

    def setBirth(self, birth):
        self.birth = birth.lower()

    #starting abilities and possessions-----------------------------------------

    #language-------------------------------------------------------------------
    def getLanguages(self):
      return self.languages

    def setLanguages(self, language, rank):
        self.languages[0] = Language(language, rank)

    def addLanguages(self, language, rank):
        self.languages.append(Language(language, rank))

    #adventuring skills---------------------------------------------------------

    #mage / non mage------------------------------------------------------------
    # REWRITE ME AFTER MAKING THE CLASS
    def getColleges(self):
      return self.colleges

    def setColleges(self, college):
        self.colleges[0] = College(college)

    def addColleges(self, college):
        self.colleges.append(College(college))

    def create(self):
        self.level = "bunny"
        self.setAllBaseStats()
        self.setAllOtherStats()
        self.calcSexMod(self.sex)
        self.calcFt(self.en)
        self.calcRacial(self.race)
        self.ep = 2500
        self.advep = 1250

    def setAllBaseStats(self):
        self.ps = int(input("PS: "))
        self.md = int(input("MD: "))
        self.ag = int(input("AG: "))
        self.ma = int(input("MA: "))
        self.wp = int(input("WP: "))
        self.en = int(input("EN: "))
        self.ft = int(input("FT: "))
        self.pc = int(input("PC: "))
        self.tmr = int(input("TMR: "))

    def setAllOtherStats(self):
        self.race = input("Race: ")
        self.na = int(input("Natural Armor: "))
        self.age = int(input("Age: "))
        self.sex = input("Sex: ")
        self.hand = input("Hand: ")
        self.ht = input("Height: ")
        self.wt = int(input("Weight: "))
        self.pb = int(input("Physical Beauty: "))
        self.aspect = input("Aspect: ")
        self.social = input("Social Status: ")
        self.birth = input("Birth Order: ")

    def calcRacial(self, race):
        if(race == "dwarf"):
            self.epmod = 1.1
            self.addRAbilities("Dwarves’ close vision is exceptionally sharp, but many have poor distance vision. They can see in the dark as a human does at dusk. Their effective range of vision in the dark is 50 feet under the open sky, 100 feet inside manmade structures, and 150 feet inside caves and tunnels.")
            self.addRAbilities("Dwarves can assess the value of and deal in gems and metals as if they are a Merchant of Rank 5. If a dwarf character progresses in the Merchant skill, their ability to assess the value of gems and metals is five greater than their current Rank, to a maximum of ten.")
            self.addRAbilities(
                "If a dwarf character is a Ranger specialising in mountains or caverns, they pay half the EP cost necessary to advance ranks.")
            self.addRAbilities(
                "A dwarf’s capacity for alcohol is twice that of a human.")
            self.ps += 2
            self.ag -= 2
            self.en += 2
            self.ma -= 2
            self.wp += 2
            self.pc += 1
            self.pb -= 2
            self.tmr -= 2

        elif(race == "elf"):
            self.epmod = 1.2
            self.addRAbilities("Elves have superior vision especially over long distances or in poor lighting. An elf can see in the dark as a human does on a cloudy day. Their effective range of vision in the dark is 150 feet under the open sky, and 75 feet elsewhere.")
            self.addRAbilities(
                "If an elf character is a ranger specialising in woods, they pay one-half the EP to advance ranks.")
            self.addRAbilities(
                "An elf receives a racial Talent which functions in all respects as the Witchcraft Witchsight Talent.")
            self.addRAbilities(
                "An elf makes little or no noise while walking and adds 10% to their chance to perform any activity requiring stealth.")
            self.addRAbilities(
                "If an elf character takes the healer skill, the elf pays three-quarters the EP to advance ranks, though they cannot resurrect the dead.")
            self.addRAbilities(
                "An elf is impervious to the special abilities of the lesser undead.")
            self.addRAbilities(
                "If an elf character takes the courtier skill, the elf pays one-half the EP to advance ranks.")
            self.ps -= 1
            self.ag += 1
            self.en -= 1
            self.ma += 1
            self.wp += 1
            self.pc += 1
            self.pb += 2
            self.tmr += 1

        elif(race == "halfling"):
            self.epmod = 1.1
            self.addRAbilities(
                "A halfling has infravision, which allows them to see faint red shapes where living beings are located in the dark. Their range of vision is 100 feet.")
            self.addRAbilities(
                "A halfling adds 20% to their chance to perform any activity requiring stealth.")
            self.addRAbilities(
                "If a halfling takes the thief skill, they pay half the EP cost to advance ranks.")
            self.addRAbilities(
                "A halfling may drop jewellery down active volcanoes without anyone thinking the worse of them.")
            self.ps -= 3
            self.md += 3
            self.ag += 1
            self.en -= 2
            self.ma -= 1
            self.wp += 1
            self.pb -= 1

        elif(race == "hill giant"):
            self.epmod = 1.5
            self.addRAbilities(
                "A giant has infravision, which allows them to see faint red shapes where living beings are located in the dark. Their range of vision is 250 feet.")
            self.addRAbilities(
                "A giant’s magic resistance is increased by 10%")
            self.addRAbilities(
                "Whenever a giant attempts minor magic, the GM should increase the difficulty factor by one, making it easier.")
            self.addRAbilities(
                "Giants may use the giant weapons listed in the Weapons Table (56.1).")
            self.ps += 7
            self.md -= 1
            self.ag -= 2
            self.en += 8
            self.ma -= 1
            self.wp -= 1
            self.ft += 1
            self.pb -= 1
            self.tmr += 3
            self.na += 1

        elif(race == "human"):
            self.epmod = 1.0
            self.addRAbilities(
                "Humans can ingratiate themselves with strangers more readily than other races. A human character has +10 to any reaction roll in an encounter with sentient creatures.")

        elif(race == "orc"):
            self.epmod = 1.1
            self.addRAbilities(
                "An orc’s eyes are highly light-sensitive. They must decrease their chance of hitting a target with Ranged Combat by 10 percent in daylight.")
            self.addRAbilities(
                "An orc has infravision, which allows them to see faint red shapes where living beings are located in the dark. Their range of vision is 150 feet.")
            self.addRAbilities(
                "Orcs are either back-stabbing scum or brutal bully-boys. An orc may take one of either Assassin Skill or Warrior Skill and pay three-quarters the EP to advance in Ranks.")
            self.addRAbilities(
                "An orc’s seed is highly fertile. The orc and hybrid orc population increase mitigates against the high orc fatality rate.")
            self.ps += 2
            self.en += 1
            self.ma -= 2
            self.wp -= 2
            self.ft += 2
            self.pb -= 4
            self.na += 1

        else:
            #shapechanger
            self.epmod = 1.4
            self.addRAbilities(
                "A shapechanger can change from human to animal form (or vice-versa) in 10 seconds during daytime and 5 seconds during the night-time.")
            self.addRAbilities(
                "A shapechanger possesses a dual nature. While in animal form, human inhibitions will be muted; while in human form, animal instincts will be dulled.")
            self.addRAbilities("A shapechanger cannot be harmed while in animal form, unless struck by a silvered weapon, magic or by a being with a Physical Strength greater than 25. Five Damage Points are automatically absorbed in the latter case.")
            self.addRAbilities(
                "A shapechanger will regenerate 1 Endurance Point every 60 seconds while in animal form.")
            self.addRAbilities("The player must devise a set of characteristics for their animal form. Take the difference between the average for each characteristic in animal and human form, and modify the human characteristics appropriately.")
            self.addRAbilities(
                "A shapechanger is automatically lunar aspected.")
            self.addRAbilities("A shapechanger can remain in animal form for a quarter of the night times the quarters of the moon showing (i.e. at full moon they may remain in animal form all night). During the day a shapechanger can remain in animal form for one hour times the quarter of the moon. A shapechanger can make one set of transformations times the quarter of the of the moon per day (i.e. dawn to next dawn).")
            self.addRAbilities("If a shapechanger is in animal form during the day, there is a 1 percent cumulative chance for each 5 minutes they remain in animal form that they will never be able to change back into human form. Similarly, if the shapechanger exceeds the time limits given above, there is a 1 percent cumulative chance (per 5 minutes) of their not being able to return to human form.")
            self.addRAbilities(
                "A shapechanger will be inconvenienced by those wards which can be used against were-creatures.")
            self.addRAbilities(
                "A shapechanger’s magic resistance is increased by 5%.")
            self.addRAbilities(
                "If a shapechanger takes the courtier skill they pay three-quarters the Experience Points necessary to advance ranks.")
            self.pb += 1

    def calcSexMod(self, sex):
        if(sex.lower() == "female"):
            self.ps -= 2
            self.md += 1
            self.en += 1

    def calcFt(self, en):
        if(en == 3 or en == 4):
            self.ft = 16
        elif(en >= 5 and en <= 7):
            self.ft = 17
        elif(en >= 8 and en <= 10):
            self.ft = 18
        elif(en >= 11 and en <= 13):
            self.ft = 19
        elif(en >= 14 and en <= 16):
            self.ft = 20
        elif(en >= 17 and en <= 19):
            self.ft = 21
        elif(en >= 20 and en <= 22):
            self.ft = 22
        elif(en >= 23 and en <= 25):
            self.ft = 23
        else:
            self.ft = 24

    def calcWeight():
        print("WIP")

    def calcHeight():
        print("WIP")

    def createRandomName(self):
        lines = open('names.txt').read().splitlines()
        return random.choice(lines)

    def createRandom(self, name):
        global raceList
        global socialList
        global aspectList

        self.level = "Bunny"
        if(name == "" or name == None):
            self.name = self.createRandomName()
        else:
            self.name = name
        self.ps = int(random.randrange(13, 16))
        self.md = int(random.randrange(13, 16))
        self.ag = int(random.randrange(13, 16))
        self.ma = int(random.randrange(13, 16))
        self.wp = int(random.randrange(13, 16))
        self.en = int(random.randrange(13, 16))
        self.ft = int(0)
        self.pc = int(5)
        self.tmr = int(5)
        #randomly pick one
        self.race = random.choice(raceList)
        self.na = int(0)
        #rand range 20+
        self.age = int(random.randrange(20, 50))
        #rand 1 or 2
        sexChoice = int(random.randrange(0, 1))
        if(sexChoice == 1):
            self.sex = "male"
        else:
            self.sex = "female"
        #roll for this
        dice1 = random.randrange(1, 5)
        dice2 = random.randrange(1, 10)
        if(dice2 > dice1):
            self.hand = "left"
        elif(dice1 == dice2):
            self.hand = "ambidextrous"
        else:
            self.hand = "right"
        #look into this later
        self.ht = "6'0 - adjust me"
        self.wt = int(random.randrange(65, 150))
        # 4d5+3 = pb
        d1 = random.randrange(1, 5)
        d2 = random.randrange(1, 5)
        d3 = random.randrange(1, 5)
        d4 = random.randrange(1, 5)
        self.pb = int(d1+d2+d3+d4+3)

        self.aspect = random.choice(aspectList)
        self.social = random.choice(socialList)
        self.birth = int(random.randrange(1, 10))
        self.calcSexMod(self.sex)
        self.calcFt(self.en)
        self.calcRacial(self.race)
        self.ep = 2500
        self.advep = 1250

    #generate a random player character
    #generate stats
    #generate race
    #calc mods
    #generate college
