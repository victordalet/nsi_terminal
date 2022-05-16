from tkinter import*
import random
from tkinter import PhotoImage

def bttn(W,x,y,text,bcolor,fcolor,cmd=None):
    """
    on créer un bouton avec du hover (réaction lorsque souris detecter)
    """

    def on_enter(e):
        """
        on change pour le clique
        """
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor

    def on_leave(e):
        """
        on change lorsque l'on enleve le clique 
        """
        mybutton['background'] = fcolor
        mybutton['foreground'] = bcolor

    #####################CONFIGURATION DU BOUTON#########################
    mybutton=Button(W,width=5,height=2,text=text,
                        fg=bcolor,
                        bg=fcolor,
                        border=0,
                        activeforeground=fcolor,
                        activebackground=bcolor,
                        command=cmd)

    ####################DETECTION CURSEUR SANS CLIQUER##########################
    mybutton.bind("<Enter>",on_enter)
    mybutton.bind("<Leave>",on_leave)
    #####################PLACE LE BOUTON#########################
    mybutton.place(x=x,y=y)




class game:
    def __init__(self):
        self.fenetre=Tk()
        self.Fond=Canvas(self.fenetre,bg='white',width=800,height=600)
        self.photoballe = []
        for i in range (2,7):
            self.photoballe.append(PhotoImage(file='boule'+str(2**i)+'.gif'))
        self.X,self.Y,self.VX,self.VY,self.r,self.balle = [],[],[],[],[],[]
        for i in range(3):
            self.X.append(random.randint(50,450))
            self.Y.append(-100)
            self.r.append(random.randint(2,6)) #le rayon sera de 2^r
            self.VX.append((-1)**random.randint(1,2)*random.randint(1,5))
            self.VY.append(random.randint(1,6))
            self.balle.append(self.Fond.create_image(self.X[i],self.Y[i],image=self.photoballe[self.r[i]-2]))
        self.position = 300
        self.vitesse = 5
        self.frame = self.Fond.create_image(self.position,450,image=PhotoImage(file='NoelG.gif'))
        bttn(self.fenetre,800/2-25,550,">","#eeeeee","#000000",self.xmore)
        bttn(self.fenetre,800/2+25,550,"<","#eeeeee","#000000",self.xless)
        self.Fond.grid()
        self.animation()
        self.fenetre.mainloop()

    def xmore(self):
        self.position += self.vitesse
        self.Fond.delete(self.frame)
        self.frame = self.Fond.create_image(self.position,450,image=PhotoImage(file='NoelG.gif'))

    def xless(self):
        self.position -= self.vitesse
        self.Fond.delete(self.frame)
        self.frame = self.Fond.create_image(self.position,450,image=PhotoImage(file='NoelD.gif'))

    def animation(self):
        i=0
        # on utilise une boucle while car le 
        # nombre de self.balle peu changer au cours de la boucle
        while i<len(self.balle):
            self.efface=False # informe que la boule i a été effacée
            self.NX=self.X[i]+self.VX[i]

            if self.NX > 800-2**self.r[i] or self.NX < 2**self.r[i]:
                self.VX[i] = -self.VX[i]
                self.NX=self.X[i]+self.VX[i]

            self.NY = self.Y[i]+self.VY[i]
            # si on tape en haut de la fenêtre ET que l'on et en train de monter
            # (car la première fois on est trop haut, mais la boule descend)
            if self.NY < 2**self.r[i] and self.VY[i] < 0 :
                self.VY[i]=-self.VY[i]
                self.NY=self.Y[i]+self.VY[i]

            if self.NY>600-2**self.r[i]: # lorsque l'on touche le sol...
                self.VY[i]=-self.VY[i]
                self.NY=self.Y[i]+self.VY[i]
                self.r[i]=self.r[i]-1

                if self.r[i]>=2: # la boule se casse en deux
                    self.Fond.itemconfig(self.balle[i],image=self.photoballe[self.r[i]-2])
                    self.NY=self.NY+2**self.r[i]

                else:
                    # si elle est trop petite, elle disparaît
                    self.Fond.delete(self.balle[i])
                    self.X.pop(i)
                    self.Y.pop(i)
                    self.r.pop(i)
                    self.VX.pop(i)
                    self.VY.pop(i)
                    self.balle.pop(i)
                    self.efface=True

            if not self.efface: # si elle n'a pas disparu, on met à jour la position
                self.X[i],self.Y[i] = self.NX,self.NY
                self.Fond.coords(self.balle[i],self.X[i],self.Y[i])
                i+=1
        # on regarde si on peut ajouter une self.balle
        n=len(self.balle)
        if n<10:
            self.X.append(random.randint(50,450))
            self.Y.append(-100)
            self.r.append(random.randint(2,6))
            self.VX.append((-1)**random.randint(1,2)*random.randint(1,5))
            self.VY.append(random.randint(1,6))
            self.balle.append(self.Fond.create_image(self.X[i],self.Y[i],image=self.photoballe[self.r[i]-2]))
        self.fenetre.after(50,self.animation)

def main():
    game()

main()