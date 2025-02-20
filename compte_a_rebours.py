import time

def countdown(n=10): # affiche un compte à rebours de n secondes, 10 par défaut
    
    while n > 0:
        print(f"Il reste {n} secondes.")  # affichage sur la même ligne
        time.sleep(1)  # pause de 1 seconde
        n -= 1
    print("Terminé !") 

countdown()