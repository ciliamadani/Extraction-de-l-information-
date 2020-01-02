import re
from bs4 import BeautifulSoup
import requests
import sys

config = open("C:/Program Files (x86)/EasyPHP-Devserver-17/eds-binaries//httpserver/apache2425vc11x86x191221155923/conf/httpd.conf", "r", encoding="utf-8")
res = open("subst.dic", "w", encoding="utf-16")
info = open("infos.txt", "w", encoding="utf-8")


alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

BonIntrv = False
# valeur de port acceptée

port = ['80','8000','8080','8008','8888']


# 2eme argument
p = sys.argv[2]
# teste de la valeur saisie
if p not in port:
    print("Port saisie erroné")
    exit(1)

port1 = "127.0.0.1:x"
port1 = port1.replace("x", p)

p1 = re.sub("127\.0\.0\.1:\d*", port1, config.read())

config.close()

config = open("C:/Program Files (x86)/EasyPHP-Devserver-17/eds-binaries//httpserver/apache2425vc11x86x191221155923/conf/httpd.conf", "w", encoding="utf-8")
config.write(p1)

# 1er argument
intrv = sys.argv[1].upper()

if len(intrv) == 3 and intrv[0] < intrv[2] and intrv[1] == '-':
      BonIntrv = True

while BonIntrv == False:
    print("Erreur! ,l'intervalle saisi est erroné, Donner l'intervalle de page que vous voulez manipuler //sous la forme A-Z//:")
    intrv = input().upper()
    if len(intrv) == 3 and intrv[0] < intrv[2] and intrv[1] == '-':
        BonIntrv = True


startIn, endIn = -1, -1
i = 0
while startIn == -1 or endIn == -1:
    if alph[i] == intrv[0]:
        startIn = i
    if alph[i] == intrv[2]:
        endIn = i
    i = i+1

alph2 = alph[startIn:endIn+1]


k = 0
for i in alph2:
    url = "http://127.0.0.1/vidal-Sommaires-Substances-#.htm".replace('#', i)
    pa = requests.get(url)
    page = pa.content
    soup = BeautifulSoup(page, 'html.parser')
    j = 0
    for a in soup.find_all("ul", attrs={"class": "substances list_index has_children"}):
        for b in a.find_all("li"):
            j = j+1
            b = b.text.strip("\n")+",.N+subst\n"
            res.write(b)
    info.write("le nombre des substances actives pour la lettre "+i+" est:"+str(j)+"\n")
    k = k+j
info.write("le nombre total d'entites medicales par substance active est :"+str(k))

res.close()
info.close()
