#completez l'ip et le port si necessaire
import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

movemode=1
ledstat=0
counter=0

def lire_json():
    global movemode
    global ledstat
    if touche=="z" :
        if movemode==1:
            print("avance")
        else:
            print("cam up")
    if touche=="s" :
        if movemode==1:
            print("recule")
        else:
            print("cam down")
    if touche=="q" :
        if movemode==1:
            print("tourne à gauche")
        else:
            print("cam left")
    if touche=="d" :
        if movemode==1:
            print("tourne à droite")
        else:
            print("cam right")
    if touche=="e" :
        if ledstat==0:
            ledstat=1
            print("alumage led :")
        else:
            ledstat=0
            print("eteignage led :")
    if touche=="sp" :
        if movemode==1:
            movemode=2
            print("mode pivot camera")
        else:
            movemode=1
            print("mode pilotage robot")
    if touche=="p" :
        print("prise des données")
        if __name__ == "__main__":
            sav_donnees_json()
            print(f"Les données ont été sauvegardées.")

def sav_donnees_json():
    global counter
    counter+=1
    donnees = {
        "date 1":{
        "temperature": round(random.uniform(15, 30), 2),  # Température entre 15°C et 30°C
        "humidite": round(random.uniform(30, 70), 2),     # Humidité relative entre 30% et 70%
        "distance": round(random.uniform(0, 100), 2),     # Distance en cm entre 0 et 100
        "taux_co2": round(random.uniform(300, 1500), 2)   # Taux de CO2 en ppm entre 300 et 1500
    }}

    with open("donnees_capteurs.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)

class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    def do_POST(self):
        global touche
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        #Traitement des données reçues
        post_data_str = post_data.decode('utf-8')  # Convertir les données en chaîne de caractères
        print("Données reçues:", post_data_str)
        post_data_json = json.loads(post_data_str)
        touche =post_data_json["touche"]
        lire_json()
        
        # Renvoyer une réponse
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {'message': 'Données reçues avec succès'}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=1707):
        server_address = ('192.168.1.20', port)
        httpd = server_class(server_address, handler_class)
        print('Serveur en écoute sur le port', port)
        httpd.serve_forever()
if __name__ == '__main__':
        run()