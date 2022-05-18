import serial #module pyserial permettant de "lire" la carte Arduino
import time #module permettant de mettre le programme en pause
from tkinter import *

oui = ""
PortARDUINO = "COM4" #On part du principe que la carte Arduino se trouve sur le port COM..
# on établit la communication série (ser)
ser = serial.Serial(PortARDUINO,9600, timeout=1) #On lit le port de la carte Arduino
def ARDOUINO():
    while True:
        ser.flushInput()
        serialValue = ser.readline().strip()
        if (len(serialValue)!=0):
            return serialValue
            break


def nouvo_label():
    sansb = ARDOUINO().split("'")
    label['text'] = f"La température est de : {sansb}°C"
    fen.after(100, nouvo_label)
fen = Tk()
fen.geometry('450x450')
fen.resizable(width=False,height=False)
label = Label(fen)
label.pack(padx=5, pady=5)
fen.after(100, nouvo_label)
fen.mainloop()
