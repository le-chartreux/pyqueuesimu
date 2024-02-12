import numpy as np

def poisson_process_simulation():
    # Paramètres
    lambda_ = 1.0 # Remplacez 1.0 par la valeur concrète de λ
    Tfin = 60 # Remplacez 60 par la durée d'observation donnée en minutes ou en secondes

    # Initialisation
    T = [-np.log(np.random.rand()) / lambda_]  # Temps d'arrivée du premier client

    # Générer les temps d'arrivée
    i = 0
    while T[i] <= Tfin:
        u = -np.log(np.random.rand()) / lambda_  # Temps entre deux arrivées consécutives
        T.append(T[i] + u)  # Temps d'arrivée du (i+1)ième client
        i += 1

    # Pour éviter d'inclure un temps d'arrivée après Tfin
    if T[-1] > Tfin:
        T.pop()

    return T