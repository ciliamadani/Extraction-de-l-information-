import re

corpus = open("corpus-medical.txt", "r", encoding="utf-8")
subst_enri = open("subst_enri.dic", "w", encoding="utf-16")
sub = open("subst.dic", "a", encoding="utf-16")
inf = open("infos2.txt", "w", encoding="utf-8")


cpts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

exp1 = "^-? ?(\w+|[A-Z]+ [A-Z]{1,3}|\w+ [A-Z]{1,3}) ?(\d+)? :? ?(\d+|,|\.)+ (mg|ml|mL|mG|MG|matin|cps|gr|g|cp/j|amp|µg|inj).+"
exp2 = "Vitamine [A-Z] ?[0-9]{0,2}|VITAMINE [A-Z] ?[0-9]{0,2}|\w+.\w+ [0-9]{1,3}g/[0-9]{1,3}mg "
exp3 = "traitement par ([A-Z]{5,15})|([A-Z]{5,15}) [0-9]{1,3} g"

cptTot = 0

# Fonction permettant de  Mettre a jour le compteur de la lettre


def majCompteur(lettre):
    cpts[lettre.lower()] = cpts[lettre.lower()] + 1


txt = []

x = re.findall(exp3, corpus.read())
for i in x:
    for j in i:
        if j != '':
            if j.lower() + ",.N+subst\n" not in txt:
                txt.append(j.lower() + ",.N+subst\n")
                # ecriture dans subst_enri
            subst_enri.write(j + ",.N+subst\n")
            # enrichissement du dic subst
            sub.write(j.lower() + ",.N+subst\n")
            cptTot = cptTot + 1
            print("-" + str(cptTot) + "  " + j)

corpus = open("corpus-medical.txt", "r", encoding="utf-8")
x = re.findall(exp2, corpus.read())
for i in x:
    if i.lower() + ",.N+subst\n" not in txt:
        txt.append(i.lower() + ",.N+subst\n")
    # ecriture dans subst_enri
    subst_enri.write(i + ",.N+subst\n")
    # enrichissement du dic subst
    sub.write(i.lower() + ",.N+subst\n")
    cptTot = cptTot + 1
    print("-"+str(cptTot)+"  "+i)

corpus = open("corpus-medical.txt", "r", encoding="utf-8")
for i in corpus:
    x = re.findall(exp1, i)
    for j in x:
        m = j[0]
        if m[0].lower() in cpts:
            # remplissage de txt a partir du corpus sans doublons
            if m.lower()+",.N+subst\n" not in txt:
                txt.append(m.lower()+",.N+subst\n")
            # ecriture dans subst_enri
            subst_enri.write(m + ",.N+subst\n")
            # enrichissement du dic subst
            sub.write(m.lower() + ",.N+subst\n")
            # affichage des entités en console avec indice
            cptTot = cptTot + 1
            print("-" + str(cptTot) + "  " + m)

subst_enri.close()
sub.close()


# Remplissage d'infos2:
cptTot = 0
for i in txt:
    cptTot = cptTot+1
    majCompteur(i[0])

for i in cpts:
    inf.write("Le nombre de médicaments issus de l’enrichissement pour la lettre "+i.upper() + " est:  " + str(cpts[i]) + "\n")
inf.write("Le nombre total de médicaments issus de l’enrichissement:  " + str(cptTot))
inf.close()

# elimination des doublons et tri du dictionnaire subst.dic:
sub = open("subst.dic", "r", encoding="utf-16")

for i in sub:
    if i not in txt:
        txt.append(i)

sub = open("subst.dic", "w", encoding="utf-16")
for i in (sorted(txt)):
    sub.write(i)
sub.close()
