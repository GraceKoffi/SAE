##############
# SAE S01.01 #
##############

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

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############


#tableau de couples d'amis
list_of_friends = ['Léo','Thierry','Léo','Valentin','Léo','Axel','Muriel','Yasmine','Muriel','Joël', 'Yasmine','Joël', 'Yasmine','Thomas','Joël','Nassim','Joël','Andrea','Joël','Ali','Nassim','Andrea','Nassim','Ali', 'Andrea','Ali','Thomas','Daria','Thomas','Carole','Thierry','Axel','Valentin','Andrea']

#tableau de couples d'amis
amis = ["Alice","Bob","Bob","Charlie","Alice","Dominique","Bob","Dominique"]

def create_network(tab):
    """ Prend en paramètre un tableau de couples d'amis et retourne le dictionnaire du réseau associé."""
    
    #initialisation des variables
    network = {}
    i = 0
    
    #on parcours tab passé en paramètre
    while i < len(tab) - 1:
        #si tab[i] n'est pas une clé de network
        if tab[i] not in network:
            network[tab[i]] = [] #l'ajouter en clé et lui mettre comme valeur un tableau vide

        #si tab[i + 1] n'est pas dans le tableau d'amis de tab[i]
        if tab[i + 1] not in network[tab[i]]:
            network[tab[i]].append(tab[i + 1]) #l'ajouter

        #si tab[i + 1] n'est pas une clé de network
        if tab[i + 1] not in network:
            network[tab[i + 1]] = [] #l'ajouter en clé et lui mettre comme valeur un tableau vide
        
        #si tab[i] n'est pas dans le tableau d'ami de tab[i + 1]
        if tab[i] not in network[tab[i + 1]]:
            network[tab[i + 1]].append(tab[i]) #l'ajouter

        i += 2

    return network

def get_people(network):
    """ Prend en paramètre un réseau et retourne la liste des personnes du reseau passé en paramètre dans un tableau."""
    #retourne un tableau contenant les clés de network
    return list(network)

def are_friends(network, person1, person2):
    """ Prend en paramètre un réseau et deux personnes.
    Retourne True si les deux personnes passé en paramètre sont amies, et False sinon."""
    
    #initialisation de variable
    i = 0
    liste = list(network)
    
    #on parcours la liste des clées de network
    while i < len(liste):
        #si person2 est dans le tableau d'amis de person1
        if person1 == liste[i] and person2 in network[person1]:
            return True
        i += 1
        
    return False

def all_his_friends(network, person, group):
    """ Prend en paramètre un réseau, une personne et un groupe de personnes.
    Retourne True si la personne passé en paramètre est amie avec toutes les personnes du groupe passé en paramètre
    et False sinon."""
    
    #si person n'est pas une clé du network
    if person not in list(network):
        return False
    
    #sinon initialisation de variable
    i = 0
    #on parcours group passé en paramètre
    while i < len(group):
        #si group[i] n'est pas dans le tableau d'amis de person
        if group[i] not in network[person]:
            return False
        i += 1
        
    return True

def is_a_community(network, group):
    """ Prend en paramètre un dictionnaire modélisant le réseau et un groupe de personnes (tableau de personnes).
    Retourne True si ce groupe est une communauté, et False sinon. """
    
    #initialisation de variable
    i = 0
    liste = list(network)
    
    #on parcours group passé en paramètre
    while i < len(group):
        #si group[i] n'est pas une clé du network
        if group[i] not in liste:
            return False
        
        #on parcours group
        while i != len(group) - 1: 
            #si d'après l'appelle de la fonction are_friends, group[i] et group[i + 1] ne sont pas amis
            if not are_friends(network, group[i], group[i + 1]):
                return False
            i += 1
            
        #si d'après l'appelle de la fonction are_friends, la première et la dernière personne de group ne sont pas amis
        if not are_friends(network, group[len(group) - 1], group[0]):
            return False
        i += 1
        
    return True

def find_community(network, group):    
    """ Prend en paramètre un réseau et un groupe de personnes et retourne une communauté en fonction de l'heuristique """
    
    #initialisation des variables
    community = []
    community.append(group[0])
    i = 1
    
    #on parcours group passé en paramètre
    while i < len(group):
        #si d'après l'appel de la fonction all_his_friends, group[i] est amis avec toutes les personnes déjà dans community
        if all_his_friends(network, group[i], community):
            community.append(group[i]) # ajouter group[i] au tableau 'community' 
          
        i += 1

    return community

def pre_order_by_decreasing_popularity(network,group,k):
    """ Prend en paramètre un réseau, un groupe de personnes et un nombre d'amis "k".
    Retourne un tableau regroupant toutes les personnes du groupe ayant "k" amis. """
    
    #initialisation des variables
    tab = []
    i = 0
    
    #on parcours group passé en paramètre
    while i < len(group):
        #si le nombre d'amis de group[i] est égale à k
        if len(network[group[i]]) == k:
            tab.append(group[i]) #ajouter la personne à tab
        i += 1
    return tab

def order_by_decreasing_popularity(network, group):
    """ Prend en paramètre un réseau et un groupe de personnes.
    Trie le groupe de personnes selon la popularité (nombre d'amis) décroissante. """
        
    #initialisation des variables
    tab = []
    i = 1
  
    #tant que l'on est pas arrivés aux nombres d'amis maximum
    while i <= nb_amis_plus_pop(network):
        #initialisation de variable
        y = 0
        #on parcours le tableau des personnes de group qui ont i amis grâce à la fonction pre_order_by_decreasing_popularity
        while y < len(pre_order_by_decreasing_popularity(network,group,i)):
            tab.append(pre_order_by_decreasing_popularity(network,group,i)[y]) #on les ajoute à tab
            y += 1
        i += 1
    tab.reverse() #on inverse tab
    return tab


def find_community_by_decreasing_popularity(network):
    """Prend en paramètre un réseau.
    Trie l'ensemble des personnes du réseau selon l'ordre décroissant de popularité.
    Retourne la communauté trouvée. """
    
    #initialisation des variables
    tab = list(network)
    f_community = [] #communauté finale
    i = 0
    
    #on parcours la liste des clés de network
    while i < len(tab):
        #initialisation des variables
        p_community = [] #communauté provisoire
        p_community.append(tab[i])
        y = 0
        #on parcours la liste des clés de network
        while y < len(tab):
            #si d'après l'appel de la fonction all_his_friends, tab[y] est amis avec toutes les personnes déjà dans p_community
            if all_his_friends(network, tab[y], p_community):
                p_community.append(tab[y]) #ajouter tab[y] dans le tableau p_community
            #si la taille de p_community est supérieur à la taille de f_community
            if len(p_community) > len(f_community):
                f_community = p_community.copy() #remplacer f_community par p_community
            y += 1
        i += 1

    return order_by_decreasing_popularity(network, find_community(network, f_community))

def find_community_from_person(network, person):
    """ Prend en paramètre un réseau et une personne.
    Retourne une communauté maximale contenant cette personne selon l'heuristique. """
   
    #initialisation des variables
    community = [person] #ajouter 'person' au tableau 'community'
    tab = list(network)
    i = 0
    
    #on parcours la liste des clés de network
    while i < len(tab):
        #si d'après l'appel de la fonction all_his_friends, tab[i] est amis avec les personnes déjà dans community
        if all_his_friends(network, tab[i], community):
            community.append(tab[i]) #ajouter tab[i] dans le tableau community
        i += 1

    return community

def find_max_community(network):
    """ Prend en paramètre un réseau.
    Retourne la plus grande communauté trouvée grâce à la fonction find_community_from_person. """
    
    #initialisation des variables
    maxCommunity = []
    liste = list(network)
    i = 0
    
    #on parcours la liste des clés de network
    while i < len(liste):
        #enregistre dans la variable community la communauté de liste[i] grâce à la fonction find_community_from_person
        community = find_community_from_person(network, liste[i])
        #si la taille de community est supérieur à la taille de maxCommunity
        if len(community) > len(maxCommunity):
            maxCommunity = community.copy() #remplacer maxCommunity par community
        i += 1

    return maxCommunity
