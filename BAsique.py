### MODULES

import serial #module pyserial permettant de "lire" la carte Arduino
import time #module permettant de mettre le programme en pause



PortARDUINO = "COM4" #On part du principe que la carte Arduino se trouve sur le port COM..

# on établit la communication série (ser)
ser = serial.Serial(PortARDUINO,9600, timeout=1) #On lit le port de la carte Arduino


while True: #Boucle infinie
    ser.flushInput()
    serialValue = ser.readline().strip()
    if (len(serialValue)!=0):#On filtre pour afficher des valeurs non nulles
        print((serialValue))

    time.sleep(2) #programme en pause 2 secondes, pour éviter d'avoir trop de valeur

