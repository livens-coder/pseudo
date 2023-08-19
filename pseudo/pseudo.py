import random
from tkinter import N, NO

print("=============================================================================")
print(".........................pwogram pou edew chwazi espsedo.....................")
print("******************************* Byenvini ************************************")
siyati = input("antre siyati w: ")
non = input("antre non ou: ")
print('----------------------------------------------------------------------------')
nonKonplet = siyati + ' ' + non
fichier = open('C:\\Users\\ADMIN1\\Desktop\\PYTHON\\pseudo\\epsedo_chwazi.txt', 'r')
fichier.seek(0)
kantite_epsedo=fichier.read().split(",")
print("Bonjou ", nonKonplet, "ou rekoni nan sevis nou an\n")
print("nou deja jenere epsedo pou " ,len(kantite_epsedo), "moun deja.\n")
fichier.close()

def premye_epsedo(nonKomplet):
    inisyal = ([non[0] for non in nonKomplet.split()])
    inisyal= ''.join(inisyal)
    inisyal=inisyal.upper()
    kantite_k = len(nonKomplet.replace(' ', ''))  
    premye = inisyal + str(kantite_k)
    return premye
premye=premye_epsedo(nonKonplet)
#print(premye_epsedo(nonKonplet))

def dezyem_epsedo(nonKomplet):
    inisyal=(siyati+non).replace('','')
    inisyal=inisyal.split()
    inisyal=''.join(inisyal)
    dezyem=inisyal.capitalize()
    return dezyem
dezyem=dezyem_epsedo(nonKonplet)

#print(dezyem_epsedo(nonKonplet))


def twazyem_epsedo(nonKomplet):
    diviz=nonKomplet.split()
    minkarate = min(diviz, key=len)
    enves = ''.join(reversed(minkarate))
    libon = enves.capitalize()
    nonmAleyatwa = str(random.randint(10, 1000))  
    twazyem = libon + nonmAleyatwa
    
    return twazyem
twazyem = twazyem_epsedo(nonKonplet)
#print(twazyem)


liste_ep=[siyati,non,premye,dezyem,twazyem]
print("lis espedo nou pwopozew la se:")
print(liste_ep)
print('')

chwa = input("Chwazi yon epsedo nan lis la: ")

while chwa not in liste_ep or len(chwa) > 7:
    print("Epsedo sa pa nan lis la oswa li gen plis pase 7 karakte.\n")
    chwa = input("Chwazi yon epsedo nan lis la: ")

fichier =open('C:\\Users\\ADMIN1\\Desktop\\PYTHON\\pseudo\\epsedo_chwazi.txt', 'a')
fichier.write(chwa + ',')
fichier.close()


print("Epsedo chwazi an anrejistre nan fichye espsedo_chwazi.")

print("----------------------------------Mesi----------------------------------------")

