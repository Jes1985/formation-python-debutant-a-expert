import string
import random

def generer(taille=10):
    speciaux = "[](){}*!;/,_-"
    caracteres = string.ascii_letters + string.digits + speciaux
    return ''.join(random.sample(caracteres, taille))

# mot_de_passe = generer(10)
# print(mot_de_passe)