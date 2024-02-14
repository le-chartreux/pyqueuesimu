import numpy as np


def depart_process_simulation(T: list[float]):
    # Paramètres
    # Remplacez 1.0 par la valeur concrète de µ
    mu = 1.0
    # Remplacez 60 par la durée d'observation donnée en minutes ou en secondes
    Tfin = 60

    # Supposons que T est la liste des temps d'arrivée des clients générée précédemment
    # Initialisation
    TS = -np.log(np.random.rand()) / mu  # Temps de service du premier client
    D = [T[0] + TS]  # Temps de départ du premier client

    # Générer les temps de départ
    i = 0
    while D[i] <= Tfin:
        TS = -np.log(np.random.rand()) / mu  # Temps de service pour le client suivant
        D.append(max(T[i + 1], D[i]) + TS)  # Temps de départ du (i+1)ième client
        i += 1
        if i >= len(T) - 1:
            # Assure que nous n'essayons pas d'accéder à un T[i+1] qui n'existe pas
            break

    # Pour éviter d'inclure un temps de départ après Tfin
    if D[-1] > Tfin:
        D.pop()

    return D
