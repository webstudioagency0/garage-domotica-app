import os
import time
from datetime import datetime
import requests

TOPIC_NTFY = "spensieri_garage"

def invia_notifica():
    ora_attuale = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messaggio = f"🚨 ALLARME GARAGE: Movimento rilevato alle {ora_attuale}!"
    requests.post(f"https://ntfy.sh/{TOPIC_NTFY}", data=messaggio.encode('utf-8'))
    print("1. Notifica ntfy inviata al telefono!")

def gestisci_movimento():
    print("Rilevato movimento!")
    ora_attuale = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Scrive nel file di log locale
    with open("log_ingressi.txt", "a") as f:
        f.write(f"[{ora_attuale}] - Movimento Rilevato (Test Mac)\n")
    print("2. Registro aggiornato sul Mac!")

    # Invia la notifica
    invia_notifica()

    # Invia le modifiche a GitHub per aggiornare il sito
    os.system("git add log_ingressi.txt")
    os.system('git commit -m "Aggiornamento log da test Mac"')
    os.system("git push origin main")
    print("3. Dati inviati a GitHub per il sito web!")

if __name__ == "__main__":
    gestisci_movimento()
