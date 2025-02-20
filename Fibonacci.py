def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        print(a, end= " ")  # affichage sur la même ligne avec un espace
        a, b = b, a + b
        i += 1
    
fibonacci(15) # exemple d'utilisation avec 15 chiffres
    