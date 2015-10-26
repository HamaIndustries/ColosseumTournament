#TODO: beginning-of-round fullStats
"""
TODO:

Magic follows the trinity of magic as normal.
Anima beats Light, Light beats Dark, and Dark beats Anima.
The individual type of Anima magic doesn't matter, in terms of magic triangle.

All Laguz use Strength as their stat of choice.
It used to be that Chromatic Dragons used Magic and targeted
Resistance, but that is no longer the case.

Constitution is it's own stat, listed in the Weapon Section of the Wiki.
Mounted/Flying Strength based units, Generals, Barons, Berserkers, and
Warriors have 10 Con, foot Strength based units have 8, Mounted/Flying
Magic users and Magic Barons have 5 Con, and Magic based foot units have 4 Con.
"""


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

    aSpeed=0
    avoid=0

    passTrigger=False
    actTrigger=False
    calc_d=False
    roundStart=False

    #temp stats
    t_strength=0
    t_skill=0
    t_speed=0
    t_luck=0
    t_defense=0
    t_resist=0
    
    t_wep_mt=0
    t_wep_hit=0
    t_wep_crit=0
    
    t_aSpeed=0
    t_avoid=0

    

    #enemy modifiers
    e_strength=0
    e_skill=0
    e_speed=0
    e_luck=0
    e_defense=0
    e_resist=0
    
    e_wep_mt=0
    e_wep_hit=0
    e_wep_crit=0
    
    e_aSpeed=0
    e_avoid=0

    #fighter modifiers

    m_strength=0
    m_skill=0
    m_speed=0
    m_luck=0
    m_defense=0
    m_resist=0
    
    m_wep_mt=0
    m_wep_hit=0
    m_wep_crit=0
    
    m_aSpeed=0
    m_avoid=0

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

    #calculates Damage, hit & crit
    #Strength (or Magic) + Weapon Might = Attack
    def calcStats(self):
        setTStats()
        self.MIGHT+=self.t_strength+self.t_wep_mt
        self.hitRate=(self.t_wep_hit+2*self.t_skill+.5*self.t_luck)-(2*self.enemy.t_speed+self.enemy.t_luck)
        self.critRate+=(self.t_wep_crit+.5*self.t_skill+5)-self.enemy.t_luck

    def prePrep(self, enemy):
        self.enemy=enemy #make sure enemy is ready

    def prep(self):
        pass     #where preround abilities trigger

    #TODO: not entirely sure what to do with this, will work on.
    def postPrep(self, enemy):
        pass 
        ##self.calc_d=True #moved here so enemy stats can be calc'd first
        #passive again
        ##calcStats()  REMOVED for calcstats be per-attack now.

    def setTStats(self):
        self.t_strength=self.strength+self.e_strength+self.m_strength
        self.t_skill=self.skill+self.e_skill+self.m_skill
        self.t_speed=self.speed+self.e_speed+self.m_speed
        self.t_luck=self.luck+self.e_luck+self.m_luck
        self.t_defense=self.defense+self.e_defense+self.m_defense
        self.t_resist=self.resist+self.e_resist+self.m_resist
    
        self.t_wep_mt=self.wep_mt+self.e_wep_mt+self.m_wep_mt
        self.t_wep_hit=self.wep_hit+self.e_wep_hit+self.m_wep_hit
        self.t_wep_crit=self.wep_crit+self.e_wep_crit+self.m_wep_crit
    
        self.t_avoid=self.avoid+e_avoid+m_avoid
        
        

class log:
    out=""
    oFile=None
    def __init__(self, f):
        self.oFile=f
    def add(self,inp):
        self.out+=str(inp)
    def clear(self):
        self.out=""
    def push(self):
        self.oFile.write("\n"+self.out)       

class actAbils:
    def cloak(target):
        pass
    def pavise(target):
        pass
    def stun(target):
        pass
    def astra(target):
        pass
    def adept(target):
        pass
    def colossus(target):
        pass
    def roar(target):
        pass
    def ignis(target):
        pass
    def tear(target):
        pass
    def impale(target):
        pass
    def flare(target):
        pass
    def sol(target):
        pass
    def luna(target):
        pass
    def flametongue(target):
        pass
    def flowing_strike(target):
        pass
    def aether(target):
        pass
    def slayer(target):
        pass
    def lethality(target):
        pass
    def bane(target):
        pass
    def counter(target):
        pass
    def maelstrom(target):
        pass
    def sure_strike(target):
        pass
    def corona(target):
        pass
    def balmwood_staff(target):
        pass
    def shadow_cloak(target):
        pass
    def dragon_blade(target):
        pass
    def vengeful_guardian(target):
        pass
    def soul_surge(target):
        pass
    def pounce(target):
        pass
    def hidden_blade(target):
        pass
    def blackfire_breath(target):
        pass
    def defense_seal(target):
        pass

class passAbils:
    def critplus(target):
        if not target.passTrigger:
            target.m_wep_crit=15
            target.passTrigger = True
    def avoidplus(target):
        if not target.passTrigger:
            target.m_avoid=20
            target.passTrigger = True
    def hpplus(target):
        if not target.passTrigger:
            target.HP+=25
            target.passTrigger = True
    def axefaire(target):
        if not target.passTrigger:
            target.m_wep_mt=5
            target.passTrigger = True
    def lancefaire(target):
        if not target.passTrigger:
            target.m_wep_mt=3
            target.m_wep_hit=10
            target.passTrigger = True
    def discipline_sword(target):
        if not target.passTrigger:
            target.m_wep_hit=20
            target.passTrigger = True
    def discipline_wind(target):
        if not target.passTrigger:
            target.m_wep_hit=20
            target.passTrigger = True
    def discipline_light(target):
        if not target.passTrigger:
            target.m_wep_hit=20
            target.passTrigger = True
    def discipline_lance(target):
        if not target.passTrigger:
            target.m_wep_hit=10
            target.m_wep_mt=2
            target.passTrigger = True
    def discipline_bow(target):
        if not target.passTrigger:
            target.m_wep_hit=10
            target.m_wep_mt=2
            target.passTrigger = True
    def discipline_thunder(target):
        if not target.passTrigger:
            target.m_wep_hit=10
            target.m_wep_mt=2
            target.passTrigger = True
    def discipline_axe(target):
        if not target.passTrigger:
            target.m_wep_mt=4
            target.passTrigger = True
    def discipline_fire(target):
        if not target.passTrigger:
            target.m_wep_mt=4
            target.passTrigger = True
    def defensive_formation(target):
        pass                     #TODO -- don't fully undertand mechanic yet
    def demoiselle(target):
        if not target.passTrigger:
            target.enemy.e_wep_hit-=15
            target.enemy.e_wep_crit-=5
            target.passTrigger=True
    def distinguished_son(target):
        if not target.passTrigger:
            target.enemy.e_wep_hit-=15
            target.enemy.e_wep_crit-=5
            target.passTrigger=True
    def daunt(target):
        if not target.passTrigger:
            target.enemy.e_wep_hit-=15
            target.enemy.e_wep_crit-=5
            target.passTrigger=True
    def patience(target):
        if not target.passTrigger and target.enemy.calc_d:
            if target.aSpeed < target.enemy.aSpeed:
                target.wep_hit+=20
                target.avoid+=20
            target.passTrigger=True
    def resolve(target):
        pass
    def wrath(target):
        pass
    def gamble(target):
         if not target.passTrigger:
            target.m_wep_crit+=25
            target.m_wep_hit-=25
            target.passTrigger=True
        pass
    def vengeance(target):
        pass
    def quick_burn(target):
        pass
    def cold_blooded(target):
        pass
    def aggressor(target):
        pass
    def limit_break(target):
        pass
    def nihil(): #possibly to be deprecated
        pass
    def toxicity(target):
        pass
    def mantle(target):
        pass
    def dragonskin(target):
        pass
    def miracle(target):
        pass
    def galeforce(target):
        pass
    def imbue(target):
        pass
    def renewal(target):
        pass
    def lifetaker(target):
        pass
    def leaching_phantom(target):
        pass
    def miasmatic_phantom(target):
        pass
    def prescient_victory(target):
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

#init fightLog
fLog = log(out)

#start of round-by-round analysis
while fitr1.HP>0 and fitr2.HP>0:
    break

out.close()
