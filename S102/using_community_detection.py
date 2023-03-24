#Question 2:
#Comparer théoriquement et expériementalement les fonctions `dico_reseau` et `create_network`.

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

#liste d'amis
amis = ["Alice", "Bob", "Bob", "Charlie", "Alice", "Dominique", "Bob", "Dominique"]

#La fonction dico_reseau est une fonction linéaire qui appelle deux autres fonctions linéaire dont une à chauque itération. On a donc une fonction quadratique.

#La fonction creare_network fait 13 opérations élémentaires à chaque itération. On a donc une fonction linéaire.

#Théoriquement la fonction creare_network est plus éfficace que la fonction dico_reseau.

from time import time

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    temps = 0
    start = time()
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    stop = time()
    temps = stop - start
    print("dico-reseau mets",round(1000*(temps),3),"ms à s'executer")
    return

def create_network(tab):
    """ prend en paramètre un tableau de couples d'amis et retourne le réseau associé."""
    temps = 0
    start = time()
    
    network = {}
    i = 0
    
    while i < len(tab) - 1:
        if tab[i] not in network:
            network[tab[i]] = []
            
        if tab[i + 1] not in network[tab[i]]:
            network[tab[i]].append(tab[i + 1])
            
        if tab[i + 1] not in network:
            network[tab[i + 1]] = []
            
        if tab[i] not in network[tab[i + 1]]:
            network[tab[i + 1]].append(tab[i])
            
        i += 2
    stop = time()
    temps = stop - start
    print("create_network mets",round(1000*(temps),3),"ms à s'executer")
    return

print(dico_reseau(amis))
print(create_network(amis))

#D'après notre experimentation, la fonction create_network est 2 fois plus rapide que la fonction dico_reseau. Notre hypothèse est donc vérifiée.

#Question 11
#Comparer théoriquement et expérimentalement les deux heuristiques de construction, celle donnée par la fonction find_community_by_decreasing_popularity et celles donnée par la fonction find_community_from_person appliquée à une personne la plus populaire (la recherche de la personne la plus populaire sera prise en compte dans la complexité).

def all_his_friends(network, person, group):
    """
    prend en paramètre un réseau, une personne et un groupe de personnes.
    retourne `True` si la personne est amie avec toutes les personnes du groupe et False sinon.
    """
    liste = list(network)
    if person not in liste:
        return False

    i = 0
    while i < len(group):
        if group[i] not in network[person]:
            return False
        i += 1

    return True

def create_network(tab):
    """ prend en paramètre un tableau de couples d'amis et retourne le réseau associé."""
    
    network = {}
    i = 0
    
    while i < len(tab) - 1:
        if tab[i] not in network:
            network[tab[i]] = []
            
        if tab[i + 1] not in network[tab[i]]:
            network[tab[i]].append(tab[i + 1])
            
        if tab[i + 1] not in network:
            network[tab[i + 1]] = []
            
        if tab[i] not in network[tab[i + 1]]:
            network[tab[i + 1]].append(tab[i])
            
        i += 2
        
    return network

amis = ["Alice", "Bob", "Bob", "Charlie", "Alice", "Dominique", "Bob", "Dominique"]

#La fonction find_community_by_decreasing_popularity est une fonction quadratique qui appelle une fonction linéaire à chaque iteration. On a donc une fonction logarithmique.

#La fonction find_community_from_person est une fonction linéaire qui appelle une fonction linéaire à chaque iteration. On a donc une fonction quadratique.

#Théoriquement la fonction find_community_from_person est plus éfficace que la fonction find_community_by_decreasing_popularity.

from time import time

def find_community_by_decreasing_popularity(network):
    '''
    prenant en paramètre un réseau.
    tri l'ensemble des personnes du réseau selon l'ordre décroissant de popularité.
    retourne la communauté trouvée.
    '''
    temps = 0
    start = time()
    
    tab = list(network)
    comunity = []
    i = 0
    while i < len(tab):
        community = []
        community.append(tab[i])
        y = 0
        while y < len(tab):
            if all_his_friends(network, tab[y], community):
                community.append(tab[y])
            if len(community) > len(comunity):
                comunity = community.copy()
            y += 1
        i += 1
    stop = time()
    temps = stop - start
    print("find_community_by_decreasing_popularity mets",round(1000*(temps),3),"ms à s'executer")
    return

def find_community_from_person(network, person):
    '''
    prend en paramètre un réseau et une personne.
    retourne une communauté maximale contenant cette personne.
    '''
    temps = 0
    start = time()
    
    community = [person]
    tab = list(network)
    i = 0
    while i < len(tab):
        if all_his_friends(network, tab[i], community):
            community.append(tab[i])
        i += 1
    stop = time()
    temps = stop - start
    print("find_community_from_person mets",round(1000*(temps),3),"ms à s'executer")
    return

print(find_community_by_decreasing_popularity(create_network(amis)))
print(find_community_from_person(create_network(amis), "Alice"))

#D'après notre experimentation, la fonction find_community_from_person est largement plus rapide que la fonction find_community_by_decreasing_popularity. Notre hypothèse est donc vérifiée.
