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


page_link = 'https://www.vidal.fr/Sommaires/Substances-&.htm'
#Modifier l'url selon la plage des valeurs voulue 


for i in range (len(subLettres)):
    pl=page_link.replace('&',subLettres[i])
    page_response = requests.get(pl, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    textContent = []
    for a in page_content.findAll("ul",attrs={"class":"substances list_index has_children"}):
        for b in a.findAll("li"):
            b=b.text.strip("\n")+",.N+subst"+"\n"
            file.write(b)
file.close()
file = open("subs.dic","r")
print(file.read())
