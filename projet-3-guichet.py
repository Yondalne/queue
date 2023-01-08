import random
import time

duree_max_service = int(time.time()) + 2*60    # duree d'activite pour le test 2min
intervalMax = 10            # duree max inter arrivee 10 sec
traitementMax = 20          # Considerans que le temps de service max est de 20sec pour le test
nb_client_recu = 0
nb_client_traite = 0
file_attente = []

def result(nb_client_recu, nb_client_traite) :
    print("\n" + ("-"*10) + " Fin du service, ce fut un plaisir ! A plus ! " + ("-"*10))    
    print("Nombre de client recu: " + str(nb_client_recu))
    print("Nombre de client traite: " + str(nb_client_traite))

def service(file_attente, nb_client_recu, nb_client_traite):
    currentTraitemnt = int(time.time()) + random.randint(1, traitementMax)
    nb_client_recu += 1
    file_attente.append(["new_client "+ str(nb_client_recu), currentTraitemnt])

    that_time = int(time.time())
    next_client = that_time + random.randint(0, intervalMax)

    left = 0
    while ((len(file_attente) > 0) and (that_time <= duree_max_service)):
        print("\nProcessing \n")
        print("Fin du traitement du " + file_attente[0][0] + " a " + time.strftime('%H:%M:%S', time.localtime(file_attente[0][1])))
        while that_time <= file_attente[0][1] :
            
            if that_time >= duree_max_service :
                break
            
            if that_time >= next_client :
                print("Nouveau client dans la file")
                nb_client_recu += 1
                traitement = that_time + random.randint(1, traitementMax)
                file_attente.append(["new_client "+ str(nb_client_recu), traitement])
                next_client = that_time + random.randint(0, intervalMax)
            else:
                left = next_client - that_time

            that_time = int(time.time())
        
        # Fin du traitment du client actuel on le retire
        print("Fin de service du client : "+ file_attente[0][0])
        
        if len(file_attente) > 1:
            print("AU SUIVANT ! ( ^ - ^ )' " + "\n")
        else :
            print("Bon bah on attend les clients =)" + "\n")
                
        file_attente.pop(0)
        nb_client_traite += 1
    return file_attente, nb_client_recu, nb_client_traite, left


next_client = int(time.time()) + random.randint(0, intervalMax)     # multiplier le rand par 60 pour mettre en min
time.sleep(random.randint(0, intervalMax))

print("Debut du test")
file_attente, nb_client_recu, nb_client_traite, left = service(file_attente, nb_client_recu, nb_client_traite)


while int(time.time() + left) <= duree_max_service:
    time.sleep(left)
    file_attente, nb_client_recu, nb_client_traite, left = service(file_attente, nb_client_recu, nb_client_traite)

result(nb_client_recu, nb_client_traite)
    