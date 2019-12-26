#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re

config = open("C:\Program Files (x86)\EasyPHP-Devserver-17\eds-binaries\httpserver\apache2425vc11x86x191226120559\conf\httpd.conf", "r", encoding="utf-8")
lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
bonInterval = False

print("Donnez le port que vous voulez utiliser:")
p = input()

port1 = "127.0.0.1:x"
port1 = port1.replace("x", p)

p1 = re.sub("127\.0\.0\.1:\d*", port1, config.read())
print(p1)
config.close()

#Modifier le port
config = open("C:/Program Files (x86)/EasyPHP-Devserver-17/eds-binaries//httpserver/apache2425vc11x86x191221155923/conf/httpd.conf", "w", encoding="utf-8")
config.write(p1)
config.close()

#Recuperer l'intervalle  des pages
while(bonInterval== False):
    print("Veuillez donner l'intervalle des pages en respectant le format suivant: X-Y")
    intrv=input().upper()
    start=intrv[0]
    end=intrv[2]
    if ( len(intrv)==3 and (start <= end) and (intrv[1]=='-')):
        bonInterval=True

#Extraire la sous liste correspondante 
startIndex,endIndex=-1,-1
i=0
while ((startIndex==-1) or (endIndex==-1)):
    if (lettres[i]==start):
        startIndex=i
    if (lettres[i]==end):
        endIndex=i
    i=i+1
        
subLettres=lettres[startIndex:endIndex+1]

file = open("subs.dic","w",encoding="utf-16")
#file.write("\ufeff")

file2 = open("infos.txt","w",encoding="utf-8")

page_link = 'http://127.0.0.1/vidal.fr/Sommaires/Substances-&.htm'
#Modifier l'url selon la plage des valeurs voulue 
cpt2=0

for i in range (len(subLettres)):
    pl=page_link.replace('&',subLettres[i])
    page_response = requests.get(pl, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    textContent = []
    for a in page_content.findAll("ul",attrs={"class":"substances list_index has_children"}):
        cpt=0
        for b in a.findAll("li"):
            b=b.text.strip("\n")+",.N+subst"+"\n"
            cpt=cpt+1
            file.write(b)
        file2.write("Le nombres des substances actives pour la letre "+subLettres[i]+" est:"+str(cpt)+"\n")
        cpt2=cpt2+cpt
file2.write("Le nombre total d'entites medicales par substance active est: "+str(cpt2))
file.close()
file2.close()

import re

corpus = open("C://Users//ezi//Desktop//L3//Extraction//corpusMedical_utf8.txt", "r", encoding="utf-8")
subst_enri = open("subst_enri.dic", "w", encoding="utf-16")
sub = open("subst.dic", "a", encoding="utf-16")

subst_enri.write("\ufeff\n")


cpts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

exps = "^-? ?(\w+) :? ?(\d+|,)+ (mg|ml).+"
j = 0

cptTot = 0


# Fonction permettant de  Mettre a jour le compteur de la lettre

def majCompteur(lettre):
    cpts[lettre.lower()] = cpts[lettre.lower()] + 1

txt=[]
for i in corpus:
    x = re.findall(exps, i)
    for j in x:
        if j[0] not in txt:
            m = j[0]
            cptTot = cptTot + 1
            subst_enri.write(m.lower() + ",.N+subst\n")
            sub.write(m.lower() + ",.N+subst\n")
            print("-" + str(cptTot) + "  " + m)
            majCompteur(m[0])

subst_enri.close()
sub.close()

# Generation d'infos2:
inf = open("infos2.txt", "w", encoding="utf-8")

for i in cpts:
    inf.write("Le nombre de médicaments issus de l’enrichissement pour la lettre "+i.upper() + " est:" + str(cpts[i]) + "\n")
inf.write("Le nombre total de médicaments issus de l’enrichissement: " + str(cptTot))
inf.close()



# elimination des doublons et tri du dictionnaire subst.dic:
sub = open("subst.dic", "r", encoding="utf-16")
tri = []
for i in sub:
    if i not in tri:
        tri.append(i)

sub = open("subst.dic", "w", encoding="utf-16")

for i in sorted(tri):
    sub.write(i)
sub.close()