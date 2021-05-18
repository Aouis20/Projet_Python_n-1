def Menu():   #MENU
  print("")
  print("")
  print("⚔️THE HUNTER AND THE HUNTED⚔️")
  print("")
  print("1: Create new game 🕹️")
  print("2: About 📜")
  print("3: Exit 🚪")
  Choix = input()
  str(Choix)
  if Choix == "1":
    Name = input("Pour commencez, veuillez entrez votre nom: ")
    Prologue(Name)
    game(Name)
  elif Choix == "2":
    About()
  elif Choix == "3":
    Exit()
  else:
    print("*Il faut rentrer un choix valide*")
    Menu()

def About():
  print("Bienvenue dans le jeu crée et développé par Aouis CHOUKRI et Yassine BENTOT, il s'agit là d'un jeu textuel.")
  print("Dans ce jeu vous incarnerez un prisonnier en cavale et les forces de l'ordre seront à vos trousses !")
  print("Vous pourrez rencontrer des ennemis ainsi que des objets qui vont aideront durant votre route.")
  print("Pour connaître la suite plongez-vous dans le jeu dès maintenant !")

def Exit():
  print("*Vous quitter le jeu...*")

def Prologue(Name):
  print("")
  print("Eh!", Name, "Tu viens de t'échapper de prison grâce au plan que t'as élaboré depuis plusieurs mois !!")
  print("Mais dépêche toi ! Tu es poursuivis par les forces de polices qui ont pour ordres de t'arrêter ou de t'exécuter si tu ne t'arrête pas.")
  print("Durant ta fuite tu devras survivre, combattre, tu trouveras des objets... Alors tâche de les utiliser à bon escient !")
  print("Tu as peu d'avance sur tes poursuivants, alors fait vite ! Ton but est de quitter le pays en rejoignant la piste d'atterrissage.")
  print("Si tu y arrives tu gagne sinon c'est la prison ou la mort qui t'attends...")

#FIN MENU
#------------DICTIONNAIRES-------------#
Affrontement = {  #Que faire ?
    1 : "⚔️ Attaquer",
    2 : "💼 Ouvrir l'inventaire",
    3 : "🏃 Fuir ?"
}

stats = { #joueur
    "Niveau" : 1,
    "XP" : 0,
    "EXP" : 250,
    "PV" : 100,
    "ATQ" : 21,
    "DEF" : 15,
}

                  #0   1   2    3          4                   5           6        7
ennemi = {        #pv #def atq xp_gagné coup renvoyer    Ennemi power      level    arme gagné
    "prisonnier" : [65,10,10,250,"ses poings","Il n'a pas l'air très coriace...",1,"Couteau (+5 ATQ)"],
    "policier" : [100,15,15,500,"son pistolet","Il n'a pas l'air très coriace...",2,"Pistolet(+8 ATQ)"],
    "militaire" : [130,25,20,750,"son fusil d'assaut","Il est à l'air surentraîné !",3,"Fusil d'assaut (+15 ATQ)"],
    "colonel" : [165,30,45,1000,"sa mitrailleuse","Il est armé jusqu'aux dents !",4,"Fusil à pompe (+25 ATQ)"],
    "BOSS" : [200,35,100,1000,"son fusil à pompe","Il n'est pas là pour plaisanter !",5,"Liberté"],
}

ennemis = { #raise
    "prisonnier" : [65,10,10,250,"ses poings","Il n'a pas l'air très coriace...",1],
    "policier" : [100,15,15,500,"son pistolet","Il n'a pas l'air très coriace...",2],
    "militaire" : [130,25,20,750,"son fusil d'assaut","Il est à l'air surentraîné !",3],
    "colonel" : [165,30,45,1000,"sa mitrailleuse","Il est armé jusqu'aux dents !",4],
    "BOSS" : [-999,35,100,1000,"son fusil à pompe","Il n'est pas là pour plaisanter !",7],
}
maxstats = {
    "PV": 100,
    "ATQ": 25,
    "DEF": 15,
}
          #bouffe
bouffe = {
    "0" : "Retour à l'inventaire",
    "1/ Bouteille d'eau 🧴 (+7 PV)": 5,
    "2/ Banane 🍌 (+15 PV)": 0,
    "3/ Pomme 🍏 (+20 PV)": 0,
    "4/ Viande 🍖 (+35 PV)": 0,
}
          #armes
weapons = {
    0 : "Retour à l'inventaire",
}

allweapons = {
    "Couteau (+5 ATQ)" : 1,
    "Pistolet(+8 ATQ)" : 0,
    "Fusil d'assaut (+15 ATQ)" : 0,
    "Fusil à pompe (+15 ATQ)": 0,
}
          #drogues
drogues = {
    0 : "Retour à l'inventaire",
    "1/ Cannabis 🍃 (+10 DEF)" : 0,
    "2/ Méth ⚗️ (+20 DEF)" : 0,
    "3/ Cocaïne 💮 (+35 DEF)" : 0,
}

#------FIGHT OU OBJET-----#
def event(case):
  event = randint(1,3)
  if event == 1 or event == 2:
    beginfight(D[case])
    raises(D[case])
  elif D[case] == "BOSS":
    beginfight("BOSS")
  else:
    Objet(case)
#----------------------------------  FIGHT  -----------------------------------#
#-----CHOIX-----#
def quefaire(en):
  print("Que veux-tu faire ?")
  for k in Affrontement:
    print(k,":",(Affrontement[k]))
  return k
#------------ MEET ---------#
def meet(en):
#ACTIONS (1)(2)(3)
  while ennemi[en][0] > 0 and stats["PV"] > 0:
    quefaire(en)
    choix = input()
    str(choix)
  #(1)Attaquer
    if choix == "1":
      infight(en)
  #(2)Inventaire   
    elif choix == "2":
      inventaire()
  #(3)Fuir
    elif choix == "3":
      fuir(en)
    else:
      print("*Il faut rentrer un choix valide*")
      meet(en)

#--------- Fuir -------#
def fuir(en):
  fuite = randint(1,5)
  if fuite == 1 :
    print("Tu essaye de t'échapper mais le",en,"a flairé t'as piste et t'as retrouvé !")
    meet(en)
  elif en == "BOSS":
    fuite = 2
    print("Tu ne peux t'échapper le BOSS ne t'en donne pas l'occasion !")
    meet(en)
  else:
    print("Le",en,"t'as perdu de vue, tu as réussi à t'échapper sans la moindre égratignure !")
    ennemi[en][0] = 0

#----------------------------------  OBJET  ----------------------------------#
def Objet(case):
  nbr = randint(1,3)
  print("Par chance, tes poursuivants ne t'ont pas retrouvés")
  if O[case] == "rien":
    print("Tu n'as rien trouvé ici...")
  else:
    print("Tu fouilles les lieux et tu trouves",nbr,O[case],"!")
    additem(case,nbr)

def additem(case,nbr):
  if O[case] == "Banane":
    bouffe["2/ Banane 🍌 (+15 PV)"]+=nbr
    stats["XP"]+=200
    exp()
  elif O[case] == "Pomme":
    bouffe["3/ Pomme 🍏 (+20 PV)"]+=nbr
    stats["XP"]+=350
    exp()
  elif O[case] == "Viande":
    bouffe["4/ Viande 🍖 (+35 PV)"]+=nbr
    stats["XP"]+=400
    exp()
  elif O[case] == "Cannabis":
    drogues["1/ Cannabis 🍃 (+10 DEF)"]+=nbr
    stats["XP"]+=200
    exp()
  elif O[case] == "Méth":
    drogues["2/ Méth ⚗️ (+20 DEF)"]+=nbr
    stats["XP"]+=300
    exp()
  elif O[case] == "Cocaïne":
    drogues["3/ Cocaïne 💮 (+35 DEF)"]+=nbr
    stats["XP"]+=400
    exp()


#------------------------------- COMBAT ------------------------------------#

from random import *

#-------------------début du combat (présentation...)
def beginfight(en):
  print("Un",en,"de niveau",ennemi[en][6],"surgit !!")
  print("STATS:","(",ennemi[en][0],"❤️ |",ennemi[en][2],"🔪 |",ennemi[en][1],"🔰 )")
  print("*Tu as (",stats["PV"],"/",maxstats["PV"],"💚 |",stats["ATQ"],"🗡️ |",stats["DEF"],"🛡️ )*")
  meet(en)

#------------------en combat (crit / atq / pv...)
def infight(en):
  crit = randint(1,4) #tx crit 25%
  encrit = randint(1,10) #ennemi tx-crit 10%
  miss = randint(1,10)
  enmiss = randint(1,10)
  monatk(en,crit,miss)
  if ennemi[en][0] > 0:
    ennemiatk(en,encrit,enmiss)
    if stats["PV"] > 0:
      print("*OUCH* Tu es dans un sale état, il te reste",stats["PV"],"/",maxstats["PV"],"💚.")
      print("")
    else:
      print("")
      print("Tu n'as plus de PV...",0,"/",maxstats["PV"],"💚.")
      
  else:
    print("")
    print("✨VICTOIRE✨")
    print("La menace a été éliminé !")
    endfight(en)

#monatq
def monatk(en,crit,miss):
  print("Tu attaques le",en,"...")
  if crit == 1 and miss != 1:
    ennemi[en][0] = ennemi[en][0] - (stats["ATQ"] - (stats["ATQ"] * ((ennemi[en][1])/100)))*2
    print("💥 COUP CRITIQUE 💥 Les dégâts sont doublés !!!")
  elif miss == 1:
    print("💨 MISS 💨 Le",en,"as esquivé ton coup.")
  else:
    ennemi[en][0] = ennemi[en][0] - (stats["ATQ"] - (stats["ATQ"] * ((ennemi[en][1])/100)))
  if ennemi[en][0] > 0:
    print("Le",en,"saigne et n'as plus que",ennemi[en][0],"❤️ !")
  else:
    print("Le",en,"est à 0 ❤️.")

#enatq
def ennemiatk(en,encrit,enmiss):
  print("Le",en,"réplique avec",ennemi[en][4],"...")
  if encrit == 1 and enmiss != 1:
    stats["PV"] = stats["PV"] - (ennemi[en][2] - (ennemi[en][2] * ((stats["DEF"])/100)))*2
    print("💣 COUP CRITIQUE 💣 Les dégâts sont doublés !!!")
  elif enmiss == 1:
    print("💨MISS💨","Tu as réussi à l'esquiver !")
  else:
    stats["PV"] = stats["PV"] - (ennemi[en][2] - (ennemi[en][2] * ((stats["DEF"])/100)))


#------------------------fin du combat (récompenses...)
def endfight(en):
  stats["ATQ"] = maxstats["ATQ"]  #reset hp après fight (if inventory)
  stats["DEF"] = maxstats["DEF"]  #reset hp après fight (if inventory)
  print("Bien joué, tu as vaincu le",en,"! Tu gagnes +",ennemi[en][3],"XP")
  stats["XP"]+=ennemi[en][3]
  exp()

#----- XP -----#
def exp():
  if stats["XP"] >= stats["EXP"] and stats["Niveau"] < 6:
    lvlup()
  elif stats["Niveau"] < 6:
    print(stats["XP"],"/", stats["EXP"],"XP, pour passer au niveau suivant !")
  else:
    print("Tu es niveau max !")

def lvlup():
  stats["Niveau"]+=1  #lvlup
  print("🆙+1: Tu es désormais niveau",stats["Niveau"],"!")
  stats["XP"]-= stats["EXP"] #reset xp
  stats["EXP"]+=250  # + xp requis pour lvl up
  maxstats["PV"]+=20        #dépassement limite ==> seuil d'hp max monte
  maxstats["ATQ"]+=8
  maxstats["DEF"]+=5
  stats["ATQ"]+=8        #augmente l'atq
  stats["DEF"]+=5        #augmente la def
  stats["PV"] = maxstats["PV"]  #regen d'hp
  print("Tes PV ont été restaurés !",stats["PV"],"/",maxstats["PV"],"💚.")
  niveau()

def niveau(): #A simplifier !
  key = 1
  if stats["Niveau"] == 2:
    bouffe["2/ Banane 🍌 (+15 PV)"]+= 3
    weapons[key] = "Couteau (+5 ATQ)",
    allweapons["Couteau (+5 ATQ)"]+=1
    drogues["1/ Cannabis 🍃 (+10 DEF)"]+=1
    print("Tu as débloqué des bananes, un couteau et du cannabis.")

  elif stats["Niveau"] == 3:
    bouffe["3/ Pomme 🍏 (+20 PV)"]+= 4
    weapons[key] = "Pistolet(+8 ATQ)"
    allweapons["Pistolet(+8 ATQ)"]+=1
    drogues["2/ Méth ⚗️ (+20 DEF)"]+=2
    print("Tu as débloqué des pommes, un pistolet et de la méth.")

  elif stats["Niveau"] == 4:
    bouffe["4/ Viande 🍖 (+35 PV)"]+= 5
    weapons[key] = "Fusil d'assaut (+15 ATQ)"
    allweapons["Fusil d'assaut (+15 ATQ)"]+=1
    drogues["3/ Cocaïne 💮 (+35 DEF)"]+=3
    print("Tu as débloqué des viandes, un fusil d'assaut et de la cocaïne.")

  elif stats["Niveau"] == 5:
    bouffe["4/ Viande 🍖 (+35 PV)"]+= 5
    drogues["3/ Cocaïne 💮 (+35 DEF)"]+=3
    print("Tu as débloqué des viandes, un fusil d'assaut et de la cocaïne.")
    print("Tu as atteint le niveau max.")

  key+=1
  return key

def raises(en): #Réanime les ennemis et lvl+1
  if ennemi[en][6] <= 2:  # >= au niveau 2
    ennemi[en] = ennemis[en]
    ennemi[en][6]+= 1
    ennemi[en][0]+= 10
    ennemi[en][1]+= 5
    ennemi[en][2]+= 7

  elif ennemi[en][6] > 3 and ennemi[en][6] <= 5: # >= au niveau 4
    ennemi[en] = ennemis[en]
    ennemi[en][6]+= 1
    ennemi[en][0]+= 10
    ennemi[en][1]+= 5
    ennemi[en][2]+= 7

  else:                       # > au niveau 5
    ennemi[en] = ennemis[en]
    ennemi[en][6]+= 1
    ennemi[en][0]+= 10
    ennemi[en][1]+= 5
    ennemi[en][2]+= 7

#Victoire
def victory(Name):
  print("Félicitation !!!")
  print("🎉🎉🎉🎉🎉")
  print("Bravo",Name,"tu as réussi à t'enfuir et tu remporte un immense cadeau, un cadeau qui n'a pas de valeur...")
  print("LA LIBÉRTÉ")
  print("🗽🕊️☮️")

#Défaite
def defeat():
  print("💀DÉFAITE💀")
  print("Ton adversaire a été plus fort que toi...")
  Menu()
#---------------------------------- Inventaire --------------------------------#
Inventaire = {
    "Niveau" : stats["Niveau"],
    0 : "Fermer l'inventaire",
    "1 / Nourriture": "(+💚)",
    "2 / Armes": "(+🗡️)",
    "3 / Drogues": "(+🛡️)",
    "4 / Quitter le jeu" : "🚪"
}

stats = {
    "Niveau" : 1,
    "XP" : 0,
    "EXP" : 250,
    "PV" : 100,
    "ATQ" : 20,
    "DEF" : 15,
}

def inventaire():
  print("💼 INVENTAIRE 💼")
  print("STATS:",stats["PV"],"/",maxstats["PV"],"💚 |",stats["ATQ"],"🗡️ |",stats["DEF"],"🛡️.")
  print("XP:",stats["XP"],"/", stats["EXP"])
  for k in Inventaire:
    print(k,":",(Inventaire[k]))
  print("")
  choice = input("Que veux-tu ? :")
  print("")
  str(choice)
  if choice == "0": #OFF
    print("*Tu as quitté l'inventaire*")
  elif choice == "1": #bouffe
    bouffes()
  elif choice == "2": #armes
    guns()
  elif choice == "3": #drogues
    drugs()
  elif choice == "4":
    Menu()
  else:             #Autre choix
    print("*Il faut rentrer un choix valide*")
    print("")
    inventaire()
  print("")


                  #-----BOUFFE / ARMES / DROGUES-----#


#//Ajout PV
def addpv(mange,pvplus,lvl):
  if bouffe[mange] > 0 and stats["PV"] < maxstats["PV"] and stats["Niveau"] >= lvl:  #HEALING
    stats["PV"]+= pvplus
    bouffe[mange]-= 1
    if stats["PV"] > maxstats["PV"]:  #LIMIT HEALING / MAXHP ==> Ne pas dépasser le maxhp
      stats["PV"] = maxstats["PV"]
    print("Tu as désormais",stats["PV"],"/",maxstats["PV"],"PV.")

  elif stats["Niveau"] < lvl:
    print("Tu n'as pas le niveau requis pour consommer cet item !")
    print("Il faut être minimum niveau",lvl,".")
    bouffes()

  elif bouffe[mange] == 0:  #EMPTY STOCK ==> Proposer autre chose à manger
    print("Tu n'en as pas en stock !")
    print("")
    bouffes()

  elif stats["PV"] == maxstats["PV"]: #FULL HP ==> retour à l'inventaire
    print("Tu es actuellement à 100% de tes PV :",stats["PV"],"/",maxstats["PV"],"PV.")
    print("")
    inventaire()


#//Choix PV
def bouffes():
  for k in bouffe:
    print(k,":",(bouffe[k]))
  choix = input("Que veux-tu ? :")
  str(choix)
  if choix == "0":  #RetourBack
    inventaire()

  elif choix == "1": #eau (+7HP)
    addpv("1/ Bouteille d'eau 🧴 (+7 PV)",7,1)
    
  elif choix == "2":  #banane (+15HP)
    addpv("2/ Banane 🍌 (+15 PV)",15,2)

  elif choix == "3":  #pomme (+20HP)
    addpv("3/ Pomme 🍏 (+20 PV)",20,3)

  elif choix == "4":  #viande (+35HP)
    addpv("4/ Viande 🍖 (+35 PV)",35,4)

  else:
    print("*Il faut rentrer un choix valide*")
    print("")
    bouffes()


#//Ajout ATQ
def addatq(arme,atqplus,lvl):
  if allweapons[arme] > 0 and stats["Niveau"] >= lvl:
    stats["ATQ"]+=atqplus
    allweapons[arme]-=1
    print("Tu as désormais",stats["ATQ"],"ATQ.")
  
  elif allweapons[arme] == 0:
    print("Tu as déjà une arme en main !")
  
  elif stats["Niveau"] < lvl:
    print("Tu n'as pas le niveau requis pour utiliser cette arme")
    print("Il faut être minimum niveau",lvl,".")
    print("")
    guns()

def addatq2(choix):
  if e == 0:
    stats["ATQ"]+= weapons[choix]
    weapons.pop(choix)
    print("Tu as désormais",stats["ATQ"],"ATQ.")
  else:
    print("Tu as déjà une arme en main")

#//Choix ATQ
def guns():
  for k in weapons:
    print(k,":",(weapons[k]))
  choix = input("Choisis ton arme: ")
  str(choix)
  if choix == "0":  #RetourBack
    inventaire()
  elif choix == "1":
    addatq("Couteau (+5 ATQ)",5,1)
  elif choix == "2":
    addatq("Fusil d'assaut (+8 ATQ)",8,3)
  elif choix == "3":
    addatq("Fusil à pompe (+15 ATQ)",12,5)
  else:
    print("*Il faut rentrer un choix valide*")
    print("")
    guns()
  print("")


#//Ajout DEF
def adddef(mange,defplus,lvl):
  if drogues[mange] > 0 and stats["Niveau"] >= lvl:  #ARMOR
    stats["DEF"]+= defplus
    drogues[mange]-= 1
    if stats["DEF"] > 65:  #LIMIT ARMOR / MAXDEF ==> Ne pas dépasser le maxdef
      stats["DEF"] = 65
      print("Tu ne peux pas dépasser 65 DEF.")
    print("Tu as désormais",stats["DEF"],"DEF.")

  elif drogues[mange] == 0:  #EMPTY STOCK ==> Proposer autre chose à manger
    print("Tu n'en as pas en stock !")
    print("")
    drugs()

  elif stats["Niveau"] < lvl:
    print("Tu n'as pas le niveau requis pour consommer cet item !")
    print("Il faut être minimum niveau",lvl,".")
    drugs()

#//Choix DEF
def drugs():
  for k in drogues:
    print(k,":",(drogues[k]))
  choix = input("Que veux-tu ? :")
  str(choix)
  if choix == "0":  #RetourBack
    inventaire()

  elif choix == "1":  #Can
    adddef("1/ Cannabis 🍃 (+10 DEF)",10,2)

  elif choix == "2": #Méth
    adddef("2/ Méth ⚗️ (+20 DEF)",20,3)

  elif choix == "3": #Coc
    adddef("3/ Cocaïne 💮 (+35 DEF)",35,4)
  
  else:
    print("*Il faut rentrer un choix valide*")
    print("")
    drugs()
  print("")

#----------------------------- MAP -----------------------------#
#Positions/Enemis
D = {
    1 : "prisonnier", #priso
    2 : "policier",
    3 : "prisonnier", #priso
    4 : "policier",
    5 : "militaire",
    6 : "policier",
    7 : "militaire",
    8 : "militaire",
    9 : "militaire",
    10 : "militaire",
    11 : "colonel",
    12 : "militaire",
    13 : "colonel",
    14 : "BOSS",
}

#Description lieux
L = { 
    1: "Tu prends la rue Fritz.",
    2: "Tu arrives à l'usine désinfecté.",
    3: "Tu prends la rue Allen.",
    4: "Te voila à la station essence.",
    5: "Tu rencontres un complice.",
    6: "Tu arrives à l'hopital.",
    7: "Tu rentres dans un lieu inexploré.",
    8: "Le gral ! Te voici à la tour magique.",
    9: "Tu explores le chantier.",
    10: "Tu rencontres un complice.",
    11 : "Tu arrives à un barage de police.",
    12 : "Génial, tu as atteint le bunker.", 
    13 : "Tu arrives à un barage de police", 
    14 : "Tu as enfin atteint la piste d'atterrissage.",
}

    
#Objet
O = {
    1 : "rien",
    2 : "rien",
    3 : "rien",
    4 : "Banane",
    5 : "Cannabis",
    6 : "Banane",
    7 : "Pomme",
    8 : "Méth",
    9 : "Méth",
    10 : "Viande",
    11 : "Cocaïne",
    12 : "Viande",
    13 : "Cocaïne",
}

#Génére une carte
def Carte (pos):
  map = [ #0 3 6 9 12          1 4 7 10 13             2 5 8 11 14          
        ["------Prison------","-----Rue Fritz----","-Usine désinfecté-"],
        ["----Rue Allen-----","--Station essence-","-----Complice-----"],
        ["------Hopital-----","-------???--------","---Tour magique---"],
        ["-----Chantier-----","-----Complice-----","-Barage de police-"],
        ["------Bunker------","-Barage de police-","Piste d'atterissage"],
        ]
  map[pos[0]][pos[1]] = "------//Toi\\-----"
  return map


def move (map,pos):
  # Affichage map
  print("")
  print("                             🗺️ MAP 🗺️")
  print("")
  for v in map:
    print(v)
    print("")
  print("")

  #Déplacement map
  i = 0
  while i < 1:
    map [pos[0]][pos[1]] = "--*Zone exploré*--"
    print("Où souhaites-tu aller ? 🧭: NORTH, EAST, SOUTH, WEST ?")
    print("")
    C = input()
    print("")
    if C == "NORTH" and pos[0] != 0:
      pos[0] = pos[0] - 1
      i = i + 1
    elif C == "SOUTH" and pos[0] != 4:
      pos[0] = pos[0] + 1
      i = i + 1
    elif C == "WEST" and pos[1] != 0 :
      pos[1] = pos[1] - 1
      i = i + 1
    elif C == "EAST" and pos[1] != 2:
      pos[1] = pos[1] + 1
      i = i + 1
    elif C == "NORTH" or C == "SOUTH" or C == "WEST" or C == "EAST":
      print("Tu ne peux pas aller par là car tu t'éloigne de l'objectif. Choisis une autre direction...")
      print("")
    else:
      print("*Il faut rentrer un choix valide*")
      print("")

    if i == 1 and map [pos[0]][pos[1]] == "--*Zone exploré*--":
      i = 0
      print("Tu es déjà passé par là. Il n'y a plus rien à explorer sur ce lieu")
      print("")
      map[pos[0]][pos[1]] = "------//Toi\\-----"
      for x in map:
        print(x)
     
  # Affichage map
  map[pos[0]][pos[1]] = "------//Toi\\-----"
  print("")
  print("                             🗺️ MAP 🗺️")
  print("")
  for x in map:
    print(x)
    print("")
  return pos

# Recherche le lieu du joueur
def Case_combat (map):
  i = 0
  c = 0
  while i < len(map):
    j = 0
    while j < len(map[i]):
      if map[i][j] == "------//Toi\\-----":
        return c
      c = c + 1
      j = j + 1
    i = i + 1

# Lance la description du lieu
def Descrip (case) :
  print("")
  print(L[case])
  print("")

#while ennemi["BOSS"][0] > 0 and stats["PV"] > 0:
def game(Name):
  # Position/Carte
  P = [0,0]
  M = Carte (P)
  #Boucle /Déplacement/Case_combat/Descrip de la case/combat sur la case
  # Gagner si boss vaincu/ perdu si joueur perd tout ses PV
  while ennemi["BOSS"][0] > 0 and stats["PV"] > 0:
    P = move (M,P)
    N = Case_combat (M)
    Descrip(N)
    event (N)
  if stats["PV"] > 0:
    victory(Name)
  else:
    defeat()
