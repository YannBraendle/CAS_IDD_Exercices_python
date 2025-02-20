import timeit

word1 = input("Entrez le mot 1: ")
word2 = input("Entrez le mot 2: ")

def common(word1, word2):
    return sorted(list(set(word1) & set(word2))) # l'utilisation de set est généralement plus rapide
# & permets de trouver les caractères communs entre les deux chaines

resultat = common(word1, word2)
print(f"les éléments communs avec la méthode 1 sont: {resultat}")

temps_common = timeit.timeit("common(word1,word2)", globals = globals(), number = 1000) 
# globals = globals() permets à la fonction timeeit d'accéder à toutes les variables du script
# number 1000 excecute l'opération 1000x pour avoir qqch de plus représentatif
print (f"Le temps pris par la fonction common pour 1000 execution est de {temps_common:.5f}")

def common2(word1, word2):
    elements_commun = []
    for i in word1:
        if i in word2 and i not in elements_commun:
            elements_commun.append(i)
    return sorted(elements_commun)

resultat2 = common2(word1, word2)
print(f"les éléments communs avec la méthode 1 sont: {resultat2}")
temps_common = timeit.timeit("common2(word1,word2)", globals = globals(), number = 1000)
print (f"Le temps pris par la fonction common2 pour 1000 execution est de {temps_common:.5f}")