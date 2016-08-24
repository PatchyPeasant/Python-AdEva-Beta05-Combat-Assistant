import random

#Eva stats
#Copy this file for as many players/angels as you need and edit stats
#Leave damage pool and critical momentum untouched unless you accidentally close the combat early.
armor = 5
toughness = 5
synchratio = 45
reflex = 30
damagepool = 0
criticalmomentum = 0
#Only there to have them defined from the begining 
evamartial = 1
evaranged = 1

#Exit loop function
def is_done():
    askend = input("End combat? [y]/[n] ")
    if askend == "y":
        return False
    return True

#Function for calculating damage, hit type, hit effect, and critical momentum.
#Allows for armor to be modified for anti-armor and armor piercing shots
def damage_calc():
    global combat
    global damagepool
    global criticalmomentum
    global armor
    global toughness
    armorhold = armor
    asklower = int(input("What is the lower bound for damage roll? "))
    askupper = int(input("What is the upper bound for the damage roll? "))
    damagemod = int(input("What is the damage modifier? "))
    askarmoreffect = input("Is the attack anti-armor [aa], armor piercing [ap], or niether [n]: ")
    if askarmoreffect == "aa":
        armor = armor // 2
    elif askarmoreffect == "ap":
        armor = 0
    damage = random.randint(asklower, askupper)
    damage = damage + damagemod
    print(damage)
    rdamage = damage - armor
    if rdamage > 0:
        damagepool = damagepool + rdamage
        criticalmomentum = damagepool//15
    if rdamage >= toughness and criticalmomentum >= 1:
        print("Critical Hit!", rdamage)
        hiteffect = random.randint(1, 10) + criticalmomentum
        print("Hit effect: ", hiteffect)
        armor = armorhold
        combat = is_done()
    elif rdamage <= toughness and rdamage > 0 or rdamage >= toughness and criticalmomentum == 0:
        print("Glancing Hit.", rdamage)
        hiteffect = random.randint(1, 6) + criticalmomentum
        print("Hit effect: ", hiteffect)
        armor = armorhold
        combat = is_done()
    elif rdamage <= 0:
        print("Hit was noselled.", rdamage)
        armor = armorhold
        combat = is_done()

#Special melee attack
def blitz_damage():
    global combat
    global damagepool
    global criticalmomentum
    global armor
    global toughness
    global martial_degree
    armorhold = armor
    asklower = int(input("What is the lower bound for damage roll? "))
    askupper = int(input("What is the upper bound for the damage roll? "))
    damagemod = int(input("What is the damage modifier? "))
    askarmoreffect = input("Is the attack anti-armor [aa], armor piercing [ap], or niether [n]: ")
    if askarmoreffect == "aa":
        armor = armor // 2
    elif askarmoreffect == "ap":
        armor = 0
    if martial_degree >= 2:
        damage1 = random.randint(asklower, askupper)
        damage1 = damage1 + damagemod
        print("Primary attack damage: ", damage1)
        damage2 = random.randint(asklower, askupper)
        damage2 = damage2 + damagemod
        print("Secondary attack damage: ", damage2)
        rdamage1 = damage1 - armor
        rdamage2 = damage2 - armor
        if rdamage1 > 0:
            damagepool = damagepool + rdamage1
            criticalmomentum = damagepool//15
        if rdamage1 >= toughness and criticalmomentum >= 1:
            print("Critical Hit!", rdamage1)
            hiteffect = random.randint(1, 10) + criticalmomentum
            print("Hit effect: ", hiteffect)
        elif rdamage1 <= toughness and rdamage1 > 0 or rdamage1 >= toughness and criticalmomentum == 0:
            print("Glancing Hit.", rdamage1)
            hiteffect = random.randint(1, 6) + criticalmomentum
            print("Hit effect: ", hiteffect)
        elif rdamage1 <= 0:
            print("Hit was noselled.", rdamage1)
        #Secondary attack starts here
        if rdamage2 > 0:
            damagepool = damagepool + rdamage2
            criticalmomentum = damagepool//15
        if rdamage2 >= toughness and criticalmomentum >= 1:
            print("(Second attack) Critical Hit!", rdamage2)
            hiteffect = random.randint(1, 10) + criticalmomentum
            print("Hit effect: ", hiteffect)
            armor = armorhold
            combat = is_done()
        elif rdamage2 <= toughness and rdamage2 > 0 or rdamage2 >= toughness and criticalmomentum == 0:
            print("(Second attack) Glancing Hit.", rdamage2)
            hiteffect = random.randint(1, 6) + criticalmomentum
            print("Hit effect: ", hiteffect)
            armor = armorhold
            combat = is_done()
        elif rdamage2 <= 0:
            print("(Second attack) Hit was noselled.", rdamage2)
            armor = armorhold
            combat = is_done()
    else:
        damage = random.randint(asklower, askupper)
        damage = damage + damagemod
        print(damage)
        rdamage = damage - armor
        if rdamage > 0:
            damagepool = damagepool + rdamage
            criticalmomentum = damagepool//15
        if rdamage >= toughness and criticalmomentum >= 1:
            print("Critical Hit!", rdamage)
            hiteffect = random.randint(1, 10) + criticalmomentum
            print("Hit effect: ", hiteffect)
            armor = armorhold
            combat = is_done()
        elif rdamage <= toughness and rdamage > 0 or rdamage >= toughness and criticalmomentum == 0:
            print("Glancing Hit.", rdamage)
            hiteffect = random.randint(1, 6) + criticalmomentum
            print("Hit effect: ", hiteffect)
            armor = armorhold
            combat = is_done()
        elif rdamage <= 0:
            print("Hit was noselled.", rdamage)
            armor = armorhold
            combat = is_done()

#Special ranged attack
def burst_damage():
    global combat
    global damagepool
    global criticalmomentum
    global armor
    global toughness
    global ranged_degree
    armorhold = armor
    asklower = int(input("What is the lower bound for damage roll? "))
    askupper = int(input("What is the upper bound for the damage roll? "))
    damagemod = int(input("What is the damage modifier? "))
    burstsize = int(input("What is the burst size of the weapon? "))
    burstdamage = int(input("What is the burst damage of the weapon? "))
    askarmoreffect = input("Is the attack anti-armor [aa], armor piercing [ap], or niether [n]: ")
    if askarmoreffect == "aa":
        armor = armor // 2
    elif askarmoreffect == "ap":
        armor = 0
    damage = random.randint(asklower, askupper)
    damage = damage + damagemod
    print("Primary attack damage (before armor): ", damage)
    rdamage = damage - armor
    if rdamage > 0:
        damagepool = damagepool + rdamage
        criticalmomentum = damagepool//15
    if rdamage >= toughness and criticalmomentum >= 1:
        print("Critical Hit!", rdamage)
        hiteffect = random.randint(1, 10) + criticalmomentum
        print("Hit effect: ", hiteffect)
    elif rdamage <= toughness and rdamage > 0 or rdamage >= toughness and criticalmomentum == 0:
        print("Glancing Hit.", rdamage)
        hiteffect = random.randint(1, 6) + criticalmomentum
        print("Hit effect: ", hiteffect)
    elif rdamage <= 0:
        print("Hit was noselled.", rdamage)
    #Secondary attack starts here
    if ranged_degree <= burstsize:
        extradamage = burstdamage * ranged_degree
    elif ranged_degree > burstsize:
        extradamage = burstdamage * burstsize
    print("Secondary attack damage (before armor): ", extradamage)
    rextradamage = extradamage - armor
    if rextradamage > 0:
        damagepool = damagepool + rextradamage
        criticalmomentum = damagepool//15
    if rextradamage >= toughness and criticalmomentum >= 1:
        print("(Second attack) Critical Hit!", rextradamage)
        hiteffect = random.randint(1, 10) + criticalmomentum
        print("Hit effect: ", hiteffect)
        armor = armorhold
        combat = is_done()
    elif rextradamage <= toughness and rextradamage > 0 or rextradamage >= toughness and criticalmomentum == 0:
        print("(Second attack) Glancing Hit.", rextradamage)
        hiteffect = random.randint(1, 6) + criticalmomentum
        print("Hit effect: ", hiteffect)
        armor = armorhold
        combat = is_done()
    elif rextradamage <= 0:
        print("(Second attack) Hit was noselled.", rextradamage)
        armor = armorhold
        combat = is_done()
        
#Hit location calculator, works well for Eva units.
#For angels with different values for target locations, you need to edit
def hitlocation_calc():
    global evamartial
    global evaranged
    global tohit
    global martial_degree
    global ranged_degree
    martialdiff = evamartial - tohit
    rangeddiff = evaranged - tohit
    martial_degree = martialdiff//10
    ranged_degree = rangeddiff//10
    if martial_degree >= 4:
        print("Hit suceeded by more than 4 degrees of freedom, attacker determines location hit.")
        askatt_type = input("Is this attack a standard attack [sa] or blitz attack [ba]? ")
        if askatt_type == "sa":
            damage_calc()
        elif askatt_type == "ba":
            blitz_damage()
    elif ranged_degree >= 4:
        print("Hit suceeded by more than 4 degrees of freedom, attacker determines location hit.")
        print(ranged_degree)
        askatt_type = input("Is this attack a standard attack [sa] or burst fire [bf]? ")
        if askatt_type == "sa":
            damage_calc()
        elif askatt_type == "bf":
            burst_damage()
    else:
        hitlocation = random.randint(1, 100)
        print("Location result:", hitlocation)
        if hitlocation <= 10:
            print("Hit head.")
            askatt_type = input("Is this attack a standard attack [sa], blitz attack [ba], or burst fire [bf]? ")
            if askatt_type == "sa":
                damage_calc()
            elif askatt_type == "bf":
                burst_damage()
            elif askatt_type == "ba":
                blitz_damage()
        elif hitlocation >= 11 and hitlocation <= 20:
            print("Hit right arm.")
            askatt_type = input("Is this attack a standard attack [sa], blitz attack [ba], or burst fire [bf]? ")
            if askatt_type == "sa":
                damage_calc()
            elif askatt_type == "bf":
                burst_damage()
            elif askatt_type == "ba":
                blitz_damage()
        elif hitlocation >= 21 and hitlocation <= 30:
            print("Hit left arm.")
            askatt_type = input("Is this attack a standard attack [sa], blitz attack [ba], or burst fire [bf]? ")
            if askatt_type == "sa":
                damage_calc()
            elif askatt_type == "bf":
                burst_damage()
            elif askatt_type == "ba":
                blitz_damage()
        elif hitlocation >= 31 and hitlocation <= 35:
            print("Hit umbilical cable (or body if none exists).")
            askatt_type = input("Is this attack a standard attack [sa], blitz attack [ba], or burst fire [bf]? ")
            if askatt_type == "sa":
                damage_calc()
            elif askatt_type == "bf":
                burst_damage()
            elif askatt_type == "ba":
                blitz_damage()
        elif hitlocation >= 36 and hitlocation <= 70:
            print("Hit body.")
            askatt_type = input("Is this attack a standard attack [sa], blitz attack [ba], or burst fire [bf]? ")
            if askatt_type == "sa":
                damage_calc()
            elif askatt_type == "bf":
                burst_damage()
            elif askatt_type == "ba":
                blitz_damage()
        elif hitlocation >= 71 and hitlocation <= 100:
            print("Hit legs.")
            askatt_type = input("Is this attack a standard attack [sa], blitz attack [ba], or burst fire [bf]? ")
            if askatt_type == "sa":
                damage_calc()
            elif askatt_type == "bf":
                burst_damage()
            elif askatt_type == "ba":
                blitz_damage()
                
#Stat adjustment section that should be asked at the beginning every time
#Allows for adjustment of armor, toughness, and synch ratio
def stat_change():
    global armor
    global toughness
    global synchratio
    askstatchange = input("Do you want to modify this unit's armor, toughness, or synch ratio? [y]/[n] ")
    if askstatchange == "y":
        print("Current armor: ", armor)
        armormod = int(input("Enter modifier: "))
        armor = armor + armormod
        print("Current toughness: ", toughness)
        toughnessmod = int(input("Enter modifier: "))
        toughness = toughness + toughnessmod
        print("Current synch ratio: ", synchratio)
        synchmod = int(input("Enter modifier: "))
        synchratio = synchratio + synchmod

#Attacking resolution
#This is used whenever this player/angel is being attacked
#It should NOT be used for this player/angel attacking
combat = True
while (combat == True):
    stat_change()
    print("Current synch ratio: ", synchratio)               
    attacktype = input("Will the attack be melee [m] or ranged [r]? ")
    if attacktype == "m":
        evamartial = int(input("What is the enemy martial score? "))
        tohit_mod = int(input("Enter modifier for attack: "))
        evamartial = evamartial + tohit_mod
        tohit = random.randint(1, 100)
        print("To hit:", tohit)
        if tohit < evamartial:
            print("Eva hit!")
            askdodge = input("Will Eva Unit guard? [y]/[n] ")
            if askdodge == "y":
                print("Eva attempted a dodge.")
                tododge = random.randint(1, 100)
                if tododge < reflex:
                    print("Eva dodged.")
                    combat = is_done()
                else:
                    print("Guard failed!")
                    hitlocation_calc()
            elif askdodge == "n":
                print("Eva didn't dodge.")
                hitlocation_calc()
        else:
            print("Enemy missed.")
            combat = is_done()
    elif attacktype == "r":
        evaranged = int(input("What is the enemy ranged score? "))
        tohit_mod = int(input("Enter modifier for attack: "))
        evaranged = evaranged + tohit_mod
        tohit = random.randint(1, 100)
        print("To hit:", tohit)
        if tohit < evaranged:
            print("Eva hit!")
            askdodge = input("Will Eva Unit guard? [y]/[n] ")
            if askdodge == "y":
                print("Eva attempted a dodge.")
                tododge = random.randint(1, 100)
                if tododge < reflex:
                    print("Eva dodged.")
                    combat = is_done()
                else:
                    print("Guard failed!")
                    hitlocation_calc()
            elif askdodge == "n":
                print("Eva didn't dodge.")
                hitlocation_calc()
        else:
            print("Enemy missed.")
            combat = is_done()
