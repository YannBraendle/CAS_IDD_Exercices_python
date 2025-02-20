def mediane():
    nombres = []
    print("Entrez un nombre par ligne, ligne vide pour terminer.")

    while True:
        nb_entres = input("Entrez un nombre: ")
        if nb_entres == "":
            break
        try:
            nb_corrects = float(nb_entres)  # convertit l'entrée en nombre flottant après vérification
            nombres.append(nb_corrects)
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    if nombres:  # vérifie que la liste n'est pas vide avant de calculer la médiane
        nombres.sort()
        n = len(nombres)
        if n % 2 == 1:
            resultat_mediane = nombres[n // 2]
        else:
            resultat_mediane = (nombres[n // 2 - 1] + nombres[n // 2]) / 2.0
        
        print(f"Vous avez entré {n} nombres. Leur médiane est {resultat_mediane:.2f}")
    else:
        print("Aucun nombre n'a été saisi.")

mediane()