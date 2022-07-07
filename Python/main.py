from tkinter import *
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from pirc522 import RFID
import time

def NFC():
    GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation (Board)
    GPIO.setwarnings(False)  # On désactive les messages d'alerte

    RFID_UID = [136, 4, 14, 56, 186]
    rc522 = RFID()  # On instancie la lib

    print(
        'En attente d\'un badge (pour quitter, Ctrl + c): ')  # On affiche un message demandant à l'utilisateur de passer son badge

    # On va faire une boucle infinie pour lire en boucle
    while True:
        rc522.wait_for_tag()  # On attnd qu'une puce RFID passe à portée
        (error, tag_type) = rc522.request()  # Quand une puce a été lue, on récupère ses infos

        if not error:  # Si on a pas d'erreur
            (error,
             uid) = rc522.anticoll()  # On nettoie les possibles collisions, ça arrive si plusieurs cartes passent en même temps
            if not error:  # Si on a réussi à nettoyer
                if RFID_UID != uid:
                    print('Paiement accepté'.format(uid))
                    label_title2.config(text="Paiement autorisé")
                    GPIO.cleanup()
                    break
                else:
                    print('Paiement refusé'.format(uid))
                    label_title2.config(text="Paiement refusé")
                    GPIO.cleanup()
                    print(uid)
                time.sleep(
                    1)  # On attend 1 seconde pour ne pas lire le tag des centaines de fois en quelques milli-secondes
                break


def correction():
    global text
    text = ""
    label_code.config(text="", font=(("04B_19_.TTF", 60)))

def validation():
    if len(text) >= 3:
        label_title2.config(text="Paiement autorisé")


#Creation fenetre
root = Tk()



root.title("YourPaD_Payement")
root.geometry("1920x1080")
root.minsize(480,1920)
root.configure(bg='white')


frame = Frame(root)
frame.config(bg=('white'))
logo = PhotoImage(file="")
label_title = Label(frame, text="YourPad", font=("04B_19_.TTF", 80), fg =("#65063E"), bg=('white'))
label_title.pack()


width=500
height=500
image = PhotoImage(file="symbole-sans-contact.png")
SansContact = Button(frame, image= image, command=NFC)
SansContact.pack()

label_title2 = Label(frame, text="Présentez carte", font=("04B_19_.TTF", 60), fg =("#65063E") , bg=('white'))
label_title2.pack(pady = 50)

frame.pack(side=TOP)

global text
text = ""


def code():
    global text
    if len(text) <= 3:
        text += "*"
        label_code.config(text = text, font=(("04B_19_.TTF", 60)))



frame_code =Frame(root, bg='white', bd=1, relief=SUNKEN)
label_code = Label(frame_code, text="Code secret", font=("04B_19_.TTF", 60), fg =("#65063E") , bg=('white'))
label_code.pack()
frame_code.pack()



frame_button1=Frame(root)

zero_button1 = Button(frame_button1, text="1", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button1.pack(side=LEFT)
zero_button2 = Button(frame_button1, text="2", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button2.pack(side=LEFT)
zero_button3 = Button(frame_button1, text="3", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button3.pack(side=LEFT)

frame_button1.pack()

frame_button2=Frame(root)

zero_button4 = Button(frame_button2, text="4", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button4.pack(side=LEFT)
zero_button5 = Button(frame_button2, text="5", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button5.pack(side=LEFT)
zero_button6 = Button(frame_button2, text="6", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button6.pack(side=LEFT)

frame_button2.pack()

frame_button3=Frame(root)

zero_button7 = Button(frame_button3, text="7", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button7.pack(side=LEFT)
zero_button8 = Button(frame_button3, text="8", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button8.pack(side=LEFT)
zero_button9 = Button(frame_button3, text="9", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button9.pack(side=LEFT)

frame_button3.pack()


zero_button = Button(root, text="0", font=("04B_19_.TTF",80), bg='#FFFCED', fg=("#65063E"), command=code)
zero_button.pack()

frame_button4=Frame()
zero_buttonA = Button(frame_button4, text="CORRECTION", font=("04B_19_.TTF",30), bg='#FFFCED', fg=("red"), command=correction)
zero_buttonA.pack(side=LEFT)
zero_buttonV = Button(frame_button4, text="VALIDER", font=("04B_19_.TTF",30), bg='#FFFCED', fg=("green"), command=validation)
zero_buttonV.pack(side=LEFT)
frame_button4.pack()





root.mainloop()



