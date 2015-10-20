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
        inL=inStr.split("\n")
        name=inL[0]
        skills=[i.replace(" ","_") for i in inL[1].split(",")]
        HP=inL[2]
        strength=inL[3]
        skills=inL[4]
        speed=inL[5]
        luck=inL[6]
        defense=inL[7]
        resist=inL[8]
        wep=inL[9]
        

    #sets enemy player for skills such as stun/defense seal/etc
    def setEnemy(self, badGuy):
        self.enemy=badGuy

class passAbils:
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

class actAbils:
    pass


class weapon:
    MIGHT = None
    HIT = None
    CRIT = None
    WEIGHT = None
    def __init__(self,typ):
        if(typ=="sword"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="lance"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="axe"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="bow"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="knife"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="light"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="fire"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="wind"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="thunder"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None
        if(typ=="dark"):
            self.MIGHT = None
            self.HIT = None
            self.CRIT = None
            self.WEIGHT = None


print("Colosseum Tournament calc v1. Remember,\nno errors are checked. Please input\nthe correct data.")
foters=open(os.path.dirname(os.path.realpath(__file__))+"input.txt","r").read().split("-------")



