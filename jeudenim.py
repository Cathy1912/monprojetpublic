import random
def allumettes(na):
    while na>0 :
        pioche=random.randint(1,3)
        print("Tu as pris",pioche," allumettes")
        montour=4-pioche
        if (na-pioche-montour)%4!=0:
            print( "j'ai perdu")
            na=0
        else :
            print("Je prends",montour,"allumettes");
            print("il reste ",na-pioche-montour, " allumettes")
            na=na-pioche-montour
            if na==0:
                print("J'ai gagné")
            elif na<4:
                montour=na
                
            else:
                print('on continue')

x=int(input("Choisis un nombre d'allumettes compris entre 4 et 20 : "  ))
allumettes(x)
