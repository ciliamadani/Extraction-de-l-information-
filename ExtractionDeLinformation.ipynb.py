#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re

lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
bonInterval = False

#Recuperer l'intervalle 
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

page_link = 'https://www.vidal.fr/Sommaires/Substances-&.htm'
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
enriFile  =open("subst_enri.dic",'w',encoding="utf-16")

#Preparer les expresssions regulieres
exps=[]
    
exps.append ("([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]{1,3} ?mg ?|([A-Z]{5,15}) [0-9]{2,4}\,|([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]{1,3} ?gr? ?")

exps.append("([A-Z]{5,15} [A-Z]{1,3}|[A-Z][a-z]{4,15} [A-Z]{1,3}) [0-9]{1,3} ?mg ?|([A-Z]{5,15} [A-Z]{1,3}|[A-Z][a-z]{4,15} [A-Z]{1,3}) [0-9]{1,3} ?gr? ")

exps.append("([A-Z]{5,15}) [0-9]{1,3} [A-Z]{1,3} |([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]\,[0-9]{1,3} ?ml ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]\.[0-9]{1,3} ?ml ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}|[a-z]{5,15}) [0-9]\,[0-9]{1,3} ?mL ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]\.[0-9]{1,3} ?mL ?")

exps.append("(\w+[a-z]{5,15}-[a-z]{4,15}) [0-9]{1,3} ?g ?/[0-9]{1,3} ?mg ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) : [0-9]{1,3} ?mg ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) ?: ?[0-9]{1,3} ?gr? ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) ?: ?[0-9]{1,3} ?ml ?")

exps.append("(Vitamine [A-Z][0-9]{0,2}) ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) [0-9]{1,4}\.[0,9]{1,4}\, ?|([A-Z]{5,15}|[A-Z][a-z]{4,15) [0-9]{1,4}\,[0,9]{1,4}\, ?|([A-Z]{5,15}) [0-9]{1,3} [0-9]{1,3} [0-9]{1,3} ?")

exps.append("Type de Stomie: ([A-Z]{4,15})")

#une dose de  ..
exps.append("une dose de ([A-Z]{4,15})")

#Traitement par
exps.append("prévention par ([A-Za-z]{4,15})|traitement par ([A-Za-z]{4,15})|traitement par([A-Z]{4,15}-[A-Z]{5,15})|traitement par([A-Z]{4,15} [A-Z]{4,15})|traitement par([A-Z]{4,15}) et ([A-Z]{4,15})|traitement par([A-Z]{4,15}), plutôt que par ([A-z]{4,15})")
exps.append("traitement par ([A-Z]{4,15}), ([A-Z]{4,15}) et ([A-Z]{4,15})")

subst_enri= open("subst_enri.dic", "w", encoding = "utf-16")
subst_enri.write("\ufeff")

rslt =[]
j=0
cptTot=0
cpts={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
      'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
##Fonction permettant de  Mettre a jour le compteur de la lettre

def majCompteur(lettre):
    cpts[lettre.lower()]=cpts[lettre.lower()]+1

for i in exps:
    corpusMedical = open("C://Users//ezi//Desktop//L3//Extraction//corpusMedical_utf8.txt",'r',encoding="utf-8")
    rslt.append (re.findall(i,corpusMedical.read()))
    for m in rslt[j]:
        for n in m:
            if n != '':
                cptTot = cptTot +1
                subst_enri.write(n+",.N+subst\n")
                #print("-"+str(cptTot)+"  "+n)
                #Mettre a jour le compteur de la lettre
                majCompteur(n[0])
                
    j=j+1     
subst_enri.close()

#Generation d'infos2
infos2= open("infos.txt","w")
infos2.write ("Le nombre de médicaments issus de l’enrichissement pour chaque lettre de l’alphabet: \n")
for i in cpts:
    infos2.write(i+"\t"+str(cpts[i])+'\n')
infos2.write("Le nombre total de médicaments issus de l’enrichissement: "+str(cptTot))
infos2.close()
