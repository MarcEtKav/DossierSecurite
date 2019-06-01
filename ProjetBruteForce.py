from itertools import chain, product
import time

force = input("entrez la force que vous voulez: ")
mot_de_passe = input("entrez le mot de passe: ")

longueur_motDePasse = len(mot_de_passe)


def BruteForce(liste_de_symbole, longueur_motDePasse):
    return (
        ''.join(symbole)
        for symbole in chain.from_iterable(product(liste_de_symbole, repeat=i)
        for i in range(1, longueur_motDePasse + 1))
        )


def BruteForceFaible():
    liste_de_symbole = "abcdefghijklmnopqrstuvwxyz"
    depart = time.time()
    for essai in BruteForce(liste_de_symbole, longueur_motDePasse):
        if essai == mot_de_passe:
            fin = time.time()
            print("Mot de passe cisco trouvé en ", round((fin - depart), 2), "secondes")
            break


def BruteForceMoyen():
    liste_de_symbole = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    depart = time.time()
    for essai in BruteForce(liste_de_symbole, longueur_motDePasse):
        if essai == mot_de_passe:
            fin = time.time()
            print("Mot de passe cisco trouvé en ", round((fin - depart), 2), "secondes")
            break


def BruteForceFort():
    liste_de_symbole = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    depart = time.time()
    for essai in BruteForce(liste_de_symbole, longueur_motDePasse):
        if essai == mot_de_passe:
            fin = time.time()
            print("Mot de passe cisco trouvé en ", round((fin - depart), 2), "secondes")
            break

if force == "faible":
    BruteForceFaible()
elif force == "moyen":
    BruteForceMoyen()
elif force == "fort":
    BruteForceFort()