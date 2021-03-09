from tkinter import *

app = Tk()
app.title('CryptoSturm')
app.geometry('800x400')
app['bg'] = '#d88900'
# Mes fonctions
def cesar(phrase, n):
    return  "".join([chr(((ord(l)-65+n)%26)+65) if l != " " else l for l in phrase.upper()])

def chiffre():
    ma_phrase = phrase.get()
    ma_phrase = ma_phrase + "e"

    sortie.set(cesar(ma_phrase, int(cle.get())))
    print(ma_phrase)

cle = StringVar()
cle.set("0")
phrase = StringVar()
phrase.set("Texte par défaut")
sortie = StringVar()
sortie.set("Sortie par défaut")
# Zone de gauche
frame_gauche = Frame(app, bg='green')
frame_gauche.pack(side=LEFT, fill=BOTH, expand=1)
label_text = Label(frame_gauche, text='Tapez votre message :')
label_text.pack(padx=2, pady=5)
zone_saisie = Entry(frame_gauche, textvariable=phrase)
zone_saisie.pack(fill=X)
label_text = Label(frame_gauche, text='Le clé :')
label_text.pack(padx=2, pady=5)
zone_saisie = Entry(frame_gauche, textvariable=cle)
zone_saisie.pack(fill=X)
bouton_chiffrer = Button(frame_gauche, text='chiffrer', bg='grey', command=chiffre)
bouton_chiffrer.pack(padx=5, pady=5, side=LEFT, fill=X)
bouton_dechiffre = Button(frame_gauche, text='Dechiffrer', bg='grey')
bouton_dechiffre.pack(padx=5, pady=5, side=RIGHT, fill=X)
#zone de droite
frame_droite = Frame(app, bg='red')
frame_droite.pack(side=RIGHT, fill=BOTH, expand=1)
label_sortie = Label(frame_droite, text='Traduction du message')
label_sortie.pack(padx=2, pady=5)
zone_sortie = Entry(frame_droite, textvariable=sortie)
zone_sortie.pack(fill=X)
bouton_quitter = Button(app, text='Ciao', command=app.destroy, bg='red')
bouton_quitter.pack(padx=5, pady=5, side=RIGHT)

app.mainloop()
