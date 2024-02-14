import numpy as np


def poisson_process_simulation():
    # Paramètres
    # Remplacez 1.0 par la valeur concrète de λ
    lambda_ = 1.0
    # Remplacez 60 par la durée d'observation donnée en minutes ou en secondes
    Tfin = 60

    # Initialisation
    T = [-np.log(np.random.rand()) / lambda_]  # Temps d'arrivée du premier client

    # Générer les temps d'arrivée
    i = 0
    while T[i] <= Tfin:
        # Temps entre deux arrivées consécutives
        u = -np.log(np.random.rand()) / lambda_
        T.append(T[i] + u)  # Temps d'arrivée du (i+1)ième client
        i += 1

    # Pour éviter d'inclure un temps d'arrivée après Tfin
    if T[-1] > Tfin:
        T.pop()

    return T
