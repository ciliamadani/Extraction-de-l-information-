# Extraction-de-l-information-
>>script Python permettant d’aspirer (collecter) les entités médicales de type noms de médicaments par substance active 
de A à Z, à partir des 26 pages HTML du dossier <<VIDAL>>

>>Générer en sortie un dictionnaire au format .dic (format DELAF vu en cours 3) encodé en UTF-16 LE avec BOM (UCS-2 LE BOM). 
>>Chaque entrée lexicale de ce dictionnaire doit être suivie par les informations (codes) ,.N+subst
>> Donner la possibilité à l’utilisateur de déterminer l’intervalle des pages à traiter, en respectant le format : 
B-H, E-S ou A-W, etc. Cet intervalle est le premier argument du premier script Python (voir « projet_1.pdf »). 
       Générer un fichier nommé « infos.txt » contenant : 
o   le nombre d’entités médicales par substance active du dictionnaire « subst.dic » généré préalablement, 
pour chaque lettre de l’alphabet ; 
o   et le nombre total d’entités médicales par substance active du dictionnaire. 
       Donner également la possibilité à l’utilisateur de saisir le port qui est précisé dans le fichier de configuration 
du serveur Web Apache. Ce port est le deuxième argument du premier script Python 
