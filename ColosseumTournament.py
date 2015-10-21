#TODO: beginning-of-round fullStats
#note to self: use dir() to check contained functions
import os
import random as r

class fighter:
    name=None
    
    #main stats
    actSkills=None
    pasSkills=None
    HP=0
    strength=0
    skill=0
    speed=0
    luck=0
    defense=0
    resist=0
    wep=None
    wepB_mt=0
    wepB_hit=0
    wepB_crit=0
    wepB_wt=0
    wepAbil=None
    fullDamage=0
    fullHit=0
    fullCrit=0

    #temp stats
    HP=0
    t_strength=0
    t_skill=0
    t_speed=0
    t_luck=0
    t_defense=0
    t_resist=0
    t_damage=0
    t_hit=0
    t_crit=0

    #enemy. set AFTER both fighters are declared,
    enemy=None

    #self explanatory.
    def __init__(self, inStr):
        inL=[i.strip() for i in inStr.split("\n")]
        try:
            for i in range(inL.count("")):
                inL.remove("")
        except Error:
            pass
        self.name=inL[0]
        self.actSkills=[i.strip().replace(" ","_").replace("+","plus").lower() for i in inL[1].split(",")]
        self.pasSkills=[i.strip().replace(" ","_").replace("+","plus").lower() for i in inL[2].split(",")]
        self.HP=int(inL[3])
        self.strength=int(inL[4])
        self.skill=int(inL[5])
        self.speed=int(inL[6])
        self.luck=int(inL[7])
        self.defense=int(inL[8])
        self.resist=int(inL[9])
        self.wep=weapon(inL[10])
        self.wep_mt=int(inL[11])+self.wep.MIGHT
        self.wep_hit=int(inL[12])*5+self.wep.HIT
        self.wep_crit=int(inL[13])*2+self.wep.CRIT
        self.wep_wt=int(inL[14])+self.wep.WEIGHT
        self.wepAbil=[i.strip().replace(" ","_").replace("+","plus").lower() if not i.strip().replace(" ","_").replace("+","plus")=="hex" else "hex_"  for i in inL[15].split(",")]
        

    #note -- TODO:
    #If Weapon Weight > Consitution, than Attack Speed = Speed - (Weapon Weight - Constitution) Otherwise, Attack Speed = Speed.
    #Avoid = (Attack Speed x 2) + Luck + bonuses (Weapon Triangle Advantage, Avoid +, Demoiselle, Flowing Strike, etc)

    #sets enemy player for skills such as stun/defense seal/etc
    def setEnemy(self, badGuy):
        self.enemy=badGuy
    

    #calculates Damage, hit & crit AFTER setenemy
    #Strength (or Magic) + Weapon Might = Attack
    def calcStats(self):
        self.fullDamage+=self.strength+self.wep_mt
        self.fullHit=(self.wep_hit+2*self.skill+.5*self.luck)-(2*self.enemy.speed+self.enemy.luck)
        self.fullCrit=(self.wep_crit+.5*self.skill+5)-self.enemy.luck

    

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

class wepAbils:
    def life_drain():
        pass
    def slayer():
        pass
    def devil():
        pass
    def panic_heal():
        pass
    def panic_damage():
        pass
    def panic_crit():
        pass
    def panic_avoid():
        pass
    def toxicity():
        pass
    def balance():
        pass
    def hex_():
        pass
    def forceweave():
        pass
    def killer():
        pass
    def dancing_weapon():
        pass
    def power_weapon():
        pass
    def shielding_weapon():
        pass
    def none():
        pass

class weapon:
    MIGHT = 0
    HIT = 0
    CRIT = 0
    WEIGHT = 0
    TYP = None
    def __init__(self,typ):
        self.TYP=typ
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
    def __str__():
        return typ

print("\nColosseum Tournament calc v1 -- normal mode.\n+--------------------------------------+\nRemember, no errors are checked. Please input the correct data.\n\n")

#Creates/opens output, writes errors to it
if (os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/output.txt")):
    os.remove(os.path.dirname(os.path.realpath(__file__))+"/output.txt")
out=open(os.path.dirname(os.path.realpath(__file__))+"/output.txt", "w+")

#Opens fighter file, reads them & creates fighter objects
try:
    foters=open(os.path.dirname(os.path.realpath(__file__))+"/input.txt","r").read().split("-------")
except IOError:
    out.write("No input.txt file found in this directory!")
    sys.exit()
    
fitr1=fighter(foters[0])
fitr2=fighter(foters[1])

#Creates seed & seeds the generator
seed=raw_input("Bash your forehead against the keyboard. Or enter random stuff, idc (seed).\n")
r.seed(seed)

#Begins to print stats

out.write("seed: "+str(seed)+"\n\n" +\
          ":----|:----|:----\n"+\
          "(stat)|"+fitr1.name+"|"+fitr2.name+\
          "\n HP|"+str(fitr1.HP)+"|"+str(fitr2.HP)+\
          "\n Damage|"+str(fitr1.fullDamage)+"|"+str(fitr2.fullDamage)+\
          "\n Hit|"+str(fitr1.fullHit)+"|"+str(fitr2.fullHit)+\
          "\n Crit|"+str(fitr1.fullCrit)+"|"+str(fitr2.fullCrit)+\
          "\n Passive Skill|"+str(fitr1.pasSkills).strip("[]").strip("\'")+"|"+str(fitr2.pasSkills).strip("[]")+\
          "\n Passive Skill|"+str(fitr1.actSkills).strip("[]").strip("\'")+"|"+str(fitr2.actSkills).strip("[]"))

#start of round-by-round analysis
while fitr1.HP>0 and fitr2.HP>0:
    print("test")
    break

out.close()
