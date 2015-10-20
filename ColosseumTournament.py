import os

class fighter:
    name=None
    
    #main stats
    HP=None
    strength=None
    skills=None
    speed=None
    luck=None
    defense=None
    resist=None
    wep=None

    #temp stats
    t_HP=None
    t_strength=None
    t_speed=None
    t_luck=None
    t_defense=None
    t_resist=None

    #enemy. set AFTER both fighters are declared,
    enemy=None

    #self explanatory.
    def __init__(self, inStr):
        inL=[i.strip().lower() for i in inStr.split("\n")]
        name=inL[0]
        skills=[i.replace(" ","_").replace("+","plus") for i in inL[1].split(",")]
        HP=inL[2]
        strength=inL[3]
        speed=inL[4]
        luck=inL[5]
        defense=inL[6]
        resist=inL[7]
        wep=inL[8]
        

    #sets enemy player for skills such as stun/defense seal/etc
    def setEnemy(self, badGuy):
        self.enemy=badGuy

class actAbils:
    def cloak():
        pass
    def pavise():
        pass
    def stun():
        pass
    def astra():
        pass
    def adept():
        pass
    def colossus():
        pass
    def roar():
        pass
    def ignis():
        pass
    def tear():
        pass
    def impale():
        pass
    def flare():
        pass
    def sol():
        pass
    def luna():
        pass
    def flametongue():
        pass
    def flowing_strike():
        pass
    def aether():
        pass
    def slayer():
        pass
    def lethality():
        pass
    def bane():
        pass
    def counter():
        pass
    def maelstrom():
        pass
    def sure_strike():
        pass
    def corona():
        pass
    def balmwood_staff():
        pass
    def shadow_cloak():
        pass
    def dragon_blade():
        pass
    def vengeful_guardian():
        pass
    def soul_surge():
        pass
    def pounce():
        pass
    def hidden_blade():
        pass
    def blackfire_breath():
        pass
    def defense_seal():
        pass

class passAbils:
    def critplus():
        pass
    def avoid():
        pass
    def hpplus():
        pass
    def axefaire():
        pass
    def lancefaire():
        pass
    def discipline_sword():
        pass
    def discipline_wind():
        pass
    def discipline_light():
        pass
    def discipline_lance():
        pass
    def discipline_bow():
        pass
    def discipline_thunder():
        pass
    def discipline_axe():
        pass
    def discipline_fire():
        pass
    def defensive_formation():
        pass
    def demoiselle():
        pass
    def distinguished():
        pass
    def patience():
        pass
    def resolve():
        pass
    def wrath():
        pass
    def gamble():
        pass
    def vengeance():
        pass
    def quick_burn():
        pass
    def cold_blooded():
        pass
    def aggressor():
        pass
    def limit_break():
        pass
    def nihil(): #possibly to be deprecated
        pass
    def toxicity():
        pass
    def mantle():
        pass
    def dragonskin():
        pass
    def miracle():
        pass
    def galeforce():
        pass
    def imbue():
        pass
    def renewal():
        pass
    def lifetaker():
        pass
    def leaching_phantom():
        pass
    def miasmatic_phantom():
        pass
    def prescient_victory():
        pass


class weapon:
    MIGHT = None
    HIT = None
    CRIT = None
    WEIGHT = None
    def __init__(self,typ):
        if(typ=="sword"):
            self.MIGHT = 1
            self.HIT = 75
            self.CRIT = 0
            self.WEIGHT = 10
        if(typ=="lance"):
            self.MIGHT = 3
            self.HIT = 70
            self.CRIT = 0
            self.WEIGHT = 11
        if(typ=="axe"):
            self.MIGHT = 5
            self.HIT = 65
            self.CRIT = 0
            self.WEIGHT = 12
        if(typ=="bow"):
            self.MIGHT = 2
            self.HIT = 70
            self.CRIT = 0
            self.WEIGHT = 12
        if(typ=="knife"):
            self.MIGHT = 0
            self.HIT = 60
            self.CRIT = 6
            self.WEIGHT = 2
        if(typ=="light"):
            self.MIGHT = 0
            self.HIT = 75
            self.CRIT = 0
            self.WEIGHT = 5
        if(typ=="fire"):
            self.MIGHT = 4
            self.HIT = 65
            self.CRIT = 0
            self.WEIGHT = 7
        if(typ=="wind"):
            self.MIGHT = 2
            self.HIT = 70
            self.CRIT = 0
            self.WEIGHT = 6
        if(typ=="thunder"):
            self.MIGHT = 3
            self.HIT = 60
            self.CRIT = 4
            self.WEIGHT = 1
        if(typ=="dark"):
            self.MIGHT = 6
            self.HIT = 55
            self.CRIT = 0
            self.WEIGHT = 7


print("Colosseum Tournament calc v1. Remember,\nno errors are checked. Please input\nthe correct data.")
foters=open(os.path.dirname(os.path.realpath(__file__))+"/input.txt","r").read().split("-------")
