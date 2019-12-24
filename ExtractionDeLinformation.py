#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import re


# In[7]:


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


# In[8]:


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


# In[92]:


corpusMedical = open("C://Users//ezi//Desktop//L3//Extraction//corpusMedical_utf8.txt",'r',encoding="utf-8")
enriFile  =open("subst_enri.dic",'w',encoding="utf-16")
#Preparer les expresssions regulieres
import re     #traitement par(([A-Z]([a-z]*\S,))*|([A-Z][a-z])*)
#traitement par (([A-Z][a-z]*),)*
#$result=re.findall("traitement par ([A-Z][a-z]{2,15})",corpusMedical.read())
#print(result)



#Traitement de sortie :
exp3="Traitement de sortie :\n ([A-Z]){4,15}\n"
#esult=re.findall(exp3,corpusMedical.read())

#Traitement a domicile :
exp44="(([A-Z]{4,15}) [0-9]+ lors des douleurs|([A-Z]{4,15}) et|(([A-Z]{4,15})/S?([A-Z]{4,15})?) : [0-9]+)|([A-Z]{4,15}) ([A-Z]+).: [0-9]+-"


result  =re.findall(exp3,corpusMedical.read())
print(result)


for i in range(len(result)):
    for j in result[i]:
        if (j!=''):
            enriFile.write(j+'\n')
            
enriFile.close()
enriFile  =open("subst_enri.dic",'r')


# In[140]:


corpusMedical = open("C://Users//ezi//Desktop//L3//Extraction//corpusMedical_utf8.txt",'r',encoding="utf-8")
enriFile  =open("subst_enri.dic",'w',encoding="utf-16")
#Preparer les expresssions regulieres

import re     
exp1 = "([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]{1,3} ?mg ?|([A-Z]{5,15}) [0-9]{2,4}\,|([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]{1,3} ?gr? ?"
exp2 = "([A-Z]{5,15} [A-Z]{1,3}|[A-Z][a-z]{4,15} [A-Z]{1,3}) [0-9]{1,3} ?mg ?|([A-Z]{5,15} [A-Z]{1,3}|[A-Z][a-z]{4,15} [A-Z]{1,3}) [0-9]{1,3} ?gr? "
exp3 = "([A-Z]{5,15}) [0-9]{1,3} [A-Z]{1,3} |([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]\,[0-9]{1,3} ?ml ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]\.[0-9]{1,3} ?ml ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}|[a-z]{5,15}) [0-9]\,[0-9]{1,3} ?mL ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}|^[a-z]{5,15}) [0-9]\.[0-9]{1,3} ?mL ?"
exp4 = "(\w+[a-z]{5,15}-[a-z]{4,15}) [0-9]{1,3} ?g ?/[0-9]{1,3} ?mg ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) : [0-9]{1,3} ?mg ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) ?: ?[0-9]{1,3} ?gr? ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) ?: ?[0-9]{1,3} ?ml ?"

exp5 = "(Vitamine [A-Z][0-9]{0,2}) ?|([A-Z]{5,15}|[A-Z][a-z]{4,15}) [0-9]{1,4}\.[0,9]{1,4}\, ?|([A-Z]{5,15}|[A-Z][a-z]{4,15) [0-9]{1,4}\,[0,9]{1,4}\, ?|([A-Z]{5,15}) [0-9]{1,3} [0-9]{1,3} [0-9]{1,3} ?"

exp6="Type de Stomie: ([A-Z]{4,15})"

#une dose de  ..
exp7="une dose de ([A-Z]{4,15})"

#Traitement par
exp8="prévention par ([A-Za-z]{4,15})|traitement par ([A-Za-z]{4,15})|traitement par([A-Z]{4,15}-[A-Z]{5,15})|traitement par([A-Z]{4,15} [A-Z]{4,15})|traitement par([A-Z]{4,15}) et ([A-Z]{4,15})|traitement par([A-Z]{4,15}), plutôt que par ([A-z]{4,15})"
exp9="traitement par ([A-Z]{4,15}), ([A-Z]{4,15}) et ([A-Z]{4,15})"

exp10="[A-Z]{5,15},|[A-Z]{5,15} [0-9]"
result=re.findall(exp7,corpusMedical.read())
print(result)



