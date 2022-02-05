from tkinter import *
from PIL import *
from random import choice
from larousse_api import larousse


class Jeu():
    def __init__(self,mot):
        
        #CREATION DE LA FENETRE
        self.fenetre = Tk()
        self.fenetre.update()
        self.fenetre.title("Jeu du pendu")
        self.fenetre.configure(bg="black")
        self.fenetre.geometry("1000x1000")
        
        #CREATION DES WIDGETS
        #CREATION DU MOT MYSTERE
        self.mot=mot
        self.mot_cache=" ".join(self.mot_underscore(self.mot))
        self.mot_cache = self.remplace(self.mot[0], self.mot, self.mot_cache)


        #LABEL POUR AFFICHER LE MOT EN UNDERSCORE
        self.var=StringVar()
        self.var.set(self.mot_cache)
        self.affiche_mots = Label (self.fenetre,textvariable = self.var,font="Times 40",bg="black",fg="white")
        self.affiche_mots.place(x=480,y=200)

        #LABEL POUR AFFICHER DES PHRASES (pour commenter le jeu)
        self.var4=StringVar()
        self.var4.set("")
        self.affiche_phrase = Label (self.fenetre,textvariable = self.var4,font="Times 14",bg="black",fg="white")
        self.affiche_phrase.place(x=500,y=400)

        #LABEL AFFICHE COUPS (affiche le nombre de coups restants)
        self.coups=8
        self.var2=IntVar()
        self.affiche_coups = Label (self.fenetre, textvariable = self.var2, font="Times 180",bg="black",fg="white")
        self.var2.set(self.coups)
        self.affiche_coups.place(x=900,y=200)

        #LABEL INDICE
        self.var6=StringVar()
        self.affiche_indice = Label (self.fenetre, textvariable = self.var6, font="Times 12",bg="black",fg="white")
        self.ind=(larousse.get_definitions(self.mot))[0]
        self.ind=self.ind.replace(self.mot,"**********")
        self.var6.set(self.ind)
        self.affiche_indice.place(x=900,y=480)
        self.affiche_indice.place_forget()

        #BOUTON INDICE
        self.bouton_indice= Button (self.fenetre, text="Indice",command=self.indice)
        self.bouton_indice.place(x=700,y=300)

        #BOUTON VALIDER
        self.bouton_valider= Button (self.fenetre, text="Valider",command=self.game)
        self.bouton_valider.place(x=550,y=350)

        #BOUTON REJOUER
        self.bouton_rejouer=Button(self.fenetre,text="Rejouer",command=self.init_welcome,padx=50,pady=10)
        self.bouton_rejouer.place(x=550,y=400)

        #CREATION DE L'ENTRY (permet à l'utilisateur d'entrer des caractères)
        self.entree1 = Entry (self.fenetre)
        self.entree1.place(x=500,y=300)
        self.entree1.bind("<Return>",self.game)
        
        #CREATION D'UN CANVAS
        self.canvas = Canvas(self.fenetre,width=300,height=350,bg="black")
        self.canvas.place(x=100,y=150)
        self.photo=PhotoImage(file="clara0.gif")
        self.photo1 = PhotoImage(file="clara1.gif")
        self.photo2 = PhotoImage(file="clara2.gif")
        self.photo3 = PhotoImage(file="clara3.gif")
        self.photo4 = PhotoImage(file="clara4.gif")
        self.photo5 = PhotoImage(file="clara5.gif")
        self.photo6 = PhotoImage(file="clara6.gif")
        self.photo7 = PhotoImage(file="clara7.gif")
        self.photo8 = PhotoImage(file="clara8.gif")
        self.i=0
        self.liste_ph=[self.photo,self.photo1,self.photo2,self.photo3,self.photo4,self.photo5,self.photo6,self.photo7,self.photo8]
        self.pic=self.canvas.create_image(152, 152, image=self.liste_ph[0])

        #CREATION D'UNE LISTE (permet de contenir les lettres déjà utilisées)
        self.lettres_utilisees=[]

        self.init_welcome("black","black","white")
        self.fenetre.mainloop()

    def init_widgets(self,mot,c1,c2):
        #CACHER LES WIDGETS DE LA PAGE WELCOME:
        self.bouton_difficile.place_forget()
        self.bouton_facile.place_forget()
        self.welcome.place_forget()
        self.bouton_aleatoire.place_forget()
        self.bouton_clair.place_forget()
        self.bouton_sombre.place_forget()

        self.fenetre.configure(bg=c2)

    
        #CREATION DU MOT
        self.mot=mot
        self.mot_cache=" ".join(self.mot_underscore(self.mot))
        self.mot_cache = self.remplace(self.mot[0], self.mot, self.mot_cache)

        #LABEL POUR AFFICHER LE MOT EN UNDERSCORE
        self.var=StringVar()
        self.var.set(self.mot_cache)
        self.affiche_mots = Label (self.fenetre,textvariable = self.var,font="Times 40",bg=c1,fg=c2)
        self.affiche_mots.place(x=480,y=200)

        #LABEL AFFICHE PHRASE (pour commenter le jeu)
        self.var4=StringVar()
        self.var4.set("")
        self.affiche_phrase = Label (self.fenetre,textvariable = self.var4,font="Times 14",bg=c1,fg=c2)
        self.affiche_phrase.place(x=550,y=400)

        #LABEL AFFICHE COUPS (affiche le nombre de coups restants)
        self.coups=8
        self.var2=IntVar()
        self.affiche_coups = Label (self.fenetre, textvariable = self.var2, font="Times 180",bg=c1,fg=c2)
        self.var2.set(self.coups)
        self.affiche_coups.place(x=1000,y=200)

         #LABEL INDICE
        self.var6=StringVar()
        self.affiche_indice = Label (self.fenetre, textvariable = self.var6, font="Times 12",bg=c1,fg=c2)
        self.ind=(larousse.get_definitions(self.mot))[0]
        self.ind=self.ind.replace(self.mot,"**********")
        self.var6.set(self.ind)
        self.affiche_indice.place(x=900,y=480)
        self.affiche_indice.place_forget()

        #BOUTON INDICE
        self.bouton_indice= Button (self.fenetre, text="Indice",command=self.indice)
        self.bouton_indice.place(x=700,y=300)

        #BOUTON VALIDER
        self.bouton_valider= Button (self.fenetre, text="Valider",command=self.game)#probleme, il marche plus 
        self.bouton_valider.place(x=550,y=350)

        #CREATION DE L'ENTRY (permet à l'utilisateur d'entrer des caractères)
        self.entree1 = Entry (self.fenetre)
        self.entree1.place(x=550,y=300)
        self.entree1.bind("<Return>",self.game)

        #CREATION D'UN CANVAS
        self.canvas = Canvas(self.fenetre,width=300,height=350,bg=c1)
        self.canvas.place(x=100,y=150)
        self.photo=PhotoImage(file="clara0.gif")
        self.photo1 = PhotoImage(file="clara1.gif")
        self.photo2 = PhotoImage(file="clara2.gif")
        self.photo3 = PhotoImage(file="clara3.gif")
        self.photo4 = PhotoImage(file="clara4.gif")
        self.photo5 = PhotoImage(file="clara5.gif")
        self.photo6 = PhotoImage(file="clara6.gif")
        self.photo7 = PhotoImage(file="clara7.gif")
        self.photo8 = PhotoImage(file="clara8.gif")
        self.i=0
        self.liste_ph=[self.photo,self.photo1,self.photo2,self.photo3,self.photo4,self.photo5,self.photo6,self.photo7,self.photo8]
        self.pic=self.canvas.create_image(152, 152, image=self.liste_ph[0])
        
        self.bouton_clair2=bttn(self.fenetre,self.fenetre.winfo_screenwidth()/2,0,"Claire","#f86263","#141414",lambda:self.init_widgets(self.mot,"white","black"))

        self.bouton_sombre2=Button(self.fenetre, text="sombre",command=lambda:self.init_widgets(self.mot,"black","white"))
        self.bouton_sombre2.place(x=900,y=400)

        #CREATION D'UNE LISTE (permet de contenir les lettres déjà utilisées)
        self.lettres_utilisees=[]

    #Fonction qui reliée au bouton indice, permet d'afficher le label indice
    def indice(self):
        self.affiche_indice.place(x=50,y=540)

    #Fonction pour générer une page de bienvenue
    def init_welcome(self,couleur1,c2,c3):
        
        #CACHER LES WIDGETS
        self.bouton_rejouer.place_forget()
        #self.affiche_coups.configure(fg="black")
        self.affiche_coups.place_forget()
        self.affiche_mots.place_forget()
        self.affiche_phrase.place_forget()
        self.bouton_valider.place_forget()
        self.entree1.place_forget()
        self.canvas.place_forget()
        self.bouton_indice.place_forget()
        self.affiche_indice.place_forget()
        self.fenetre.configure(bg=c2)
        self.bouton_clair=Button(self.fenetre, text="Mode clair",command=lambda:self.init_welcome("white","white","black"))
        self.bouton_clair.place(x=700,y=300)

        self.bouton_sombre=Button(self.fenetre, text="Mode sombre",command=lambda:self.init_welcome("black","black","white"))
        self.bouton_sombre.place(x=700,y=400)


        #LABEL DE BIENVENUE
        self.var0=StringVar()
        self.welcome = Label (self.fenetre,textvariable = self.var0,font="Times 30",bg=couleur1,fg=c3)
        self.var0.set("Bienvenue dans le jeu du pendu !\nVeuillez choisir votre mode de jeu.")
        self.welcome.place(x=380,y=150)

        #BOUTON FACILE
        self.motfacile=mot_a_trouver()
        self.bouton_facile= Button (self.fenetre, text="Facile",font="Times",command=lambda:self.init_widgets(self.motfacile,"pink","black"),padx=20,pady=20,bg="lightgreen")
        self.bouton_facile.place(x=420,y=400)

        #BOUTON DIFFICILE
        self.motdiff=mot_difficile()
        self.bouton_difficile= Button (self.fenetre, text="Difficile",font="Times",command=lambda:self.init_widgets(self.motdiff,"green","white"),padx=20,pady=20,bg="lightpink")
        self.bouton_difficile.place(x=620,y=400)

        #BOUTON ALEATOIRE
        self.mot_ale=hasard()
        self.bouton_aleatoire= Button (self.fenetre, text="Aléatoire",font="Times",command=lambda:self.init_widgets(self.mot_ale,"blue","white"),padx=20,pady=20,bg="lightblue")
        self.bouton_aleatoire.place(x=820,y=400)
    

    def mot_underscore(self,mot):
        mot_cache = ""
        for i in range(len(mot)):
            mot_cache += "_"
        return mot_cache

    def remplace(self,lettre,msecret,cache):
        for i in range(len(msecret)):
            if msecret[i] == lettre:
                t = list(cache) 
                t[2*i] = lettre #pour eviter que ça remplace les espaces 
                cache = "".join(t)
        return cache

    def est_valide(self,mot):
        for c in mot:
            if not c.isalpha():
                return True
            else:
                return False

    #Fonction principale du jeu
    def game(self,event=None):#event pour pouvoir executer "self.entree1.bind("<Return>",self.game)" sans problème

        #PHRASES POUR LES COMMENTAIRES
        phrase0="Raté! Il vous reste "+str(self.coups-1)+" coup(s)"
        phrase1="Dommage...Le mot était "+str(self.mot)
        phrase2="Bravo! Le mot était bien "+str(self.mot)
        phrase3="Lettre déjà utilisée.⚠️"
        phrase4="Le caractère entré n'est pas valide.⚠️"
        phrase5="Bien vu!"
        phrase6="BRAVO"

        lettre=self.entree1.get()
        self.entree1.delete(0, END)
        # if self.mot in self.var6:
        #   self.var6.set(self.var6-self.mot)

        if len(lettre)>1 or self.est_valide(lettre):
            self.var4.set(phrase4)
            if lettre==self.mot:
                self.var.set(self.mot)
                self.bouton_rejouer.place(x=500,y=450)
                self.var4.set(phrase6)
        elif "_" in self.mot_cache:
            if self.coups>0:
                    if lettre in self.mot:
                        if lettre in self.lettres_utilisees:
                            self.var4.set(phrase3)
                        else:
                            self.mot_cache=self.remplace(lettre,self.mot,self.mot_cache)
                            self.var.set(self.mot_cache)
                            self.var4.set(phrase5)
                            self.lettres_utilisees.append(lettre)#utiliser time
                        if "_" not in self.mot_cache:
                            self.var4.set(phrase2)
                            self.bouton_rejouer.place(x=500,y=450)
                    else :
                        if lettre in self.lettres_utilisees:
                            self.var4.set(phrase3)
                        else:   
                            self.coups -= 1
                            if self.coups==0:
                                self.pic=self.canvas.create_image(152, 152, image=self.liste_ph[8])
                                self.var2.set(self.coups)
                                self.var4.set(phrase1)
                                self.bouton_rejouer.place(x=500,y=450)
                            else:
                                self.var2.set(self.coups)
                                self.i+=1
                                self.pic=self.canvas.create_image(152, 152, image=self.liste_ph[self.i])
                                self.canvas.place(x=100,y=150)
                                self.var4.set(phrase0)
                                self.lettres_utilisees.append(lettre)  