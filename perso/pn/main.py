from tkinter import*
import random
import time
import json

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
    mybutton=Button(W,width=9,height=2,text=text,
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
    return mybutton



def import_data(url):
    """
    get data
    input : url (str)
    output : data (list 2d)
    """
    with open(url) as read_file:
        data = json.load(read_file)
    return data

def give_data(url,data):
    """
    remplace un fichier json par une nouvelle valeur
    """
    with open(url,"w") as fp:
        json.dump(data,fp)


class game:
    def __init__(self,mode=0):
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
        self.vitesse = 20
        self.win = 3
        self.mode = mode
        self.droit = True
        self.gauche = True
        self.time_d = round(time.time())
        if mode: self.btn_time = bttn(self.fenetre,1,1,str(round(time.time())-self.time_d),"#eeeeee","#000000")
        else : self.btn_time = bttn(self.fenetre,1,1,str(60-(round(time.time())-self.time_d)),"#eeeeee","#000000")
        self.btn_heart = bttn(self.fenetre,750,1,str(self.win),"#eeeeee","#000000")
        if self.mode : bttn(self.fenetre,680,1,"record : "+str(import_data('score.json')),"#eeeeee","#000000")
        self.picture('NoelG.gif')
        bttn(self.fenetre,800/2-40,20,"<","#eeeeee","#000000",self.xless)
        bttn(self.fenetre,800/2+25,20,">","#eeeeee","#000000",self.xmore)
        self.Fond.grid()
        self.animation()
        self.fenetre.mainloop()

    def xmore(self):    
        if self.win != False:
            if self.droit:
                self.position += self.vitesse
                self.picture('NoelD.gif')

    def xless(self):
        if self.win != False:
            if self.gauche:
                self.position -= self.vitesse
                self.picture('NoelG.gif')

    def wall(self):
        if self.air_pn()[0] <= 0:
            self.gauche = False
        else: 
            self.gauche = True
        if self.air_pn()[1] >= 800:
            self.droit = False
        else:
            self.droit = True 

    def animation(self):
        i=0
        # on utilise une boucle while car le 
        # nombre de self.balle peu changer au cours de la boucle
        while i<len(self.balle) and self.win != False:
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
                self.game_over(i)
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
        self.time()
        self.heart()
        self.wall()
        self.fenetre.after(50,self.animation)

    def picture(self,url):
        self.img = PhotoImage(file=url)
        self.image = Label(image=self.img).place(x=self.position,y=450)

    def air_boule(self,i):
        return self.X[i]-self.r[i],self.X[i]+self.r[i],self.Y[i]-self.r[i],self.Y[i]+self.r[i]

    def air_pn(self):
        return self.position,self.position+88,450,600

    def collision(self,i):
        if (self.air_pn()[0] <= self.air_boule(i)[0] <= self.air_pn()[1] or self.air_pn()[0] <= self.air_boule(i)[1] <= self.air_pn()[1]) and (self.air_pn()[2] <= self.air_boule(i)[2] <= self.air_pn()[3] or self.air_pn()[2] <= self.air_boule(i)[3] <= self.air_pn()[3]):
            return 1
        return 0

    def game_over(self,i): 
        test = self.collision(i)
        self.win -= test
        if test:
            self.Fond.delete(self.balle[i])
            self.X.pop(i)
            self.Y.pop(i)
            self.r.pop(i)
            self.VX.pop(i)
            self.VY.pop(i)
            self.balle.pop(i)   
            self.efface=True
        if self.win == False:
            self.btn_retry = bttn(self.fenetre,400,300,"retry","#eeeeee","#000000",self.retry)
            if self.mode:
                if round(time.time())-self.time_d > import_data('score.json'):
                    give_data('score.json',round(time.time())-self.time_d)
            else:
                bttn(self.fenetre,400,330,"Perdu","#eeeeee","#000000")


    def retry(self):
        self.btn_retry.destroy()
        self.fenetre.destroy()
        game()

    def time(self):
        if self.win != False:
            self.btn_time.destroy()
            if self.mode:
                self.btn_time = bttn(self.fenetre,1,1,str(round(time.time())-self.time_d),"#eeeeee","#000000")
            else:
                self.btn_time = bttn(self.fenetre,1,1,str(60-(round(time.time())-self.time_d)),"#eeeeee","#000000")
                if 60-(round(time.time())-self.time_d) <= 0:
                    self.btn_retry = bttn(self.fenetre,400,300,"retry","#eeeeee","#000000",self.retry)
                    bttn(self.fenetre,400,330,"Gagné","#eeeeee","#000000")
                    self.win = False


    def heart(self):
        self.btn_heart.destroy()
        self.btn_heart = bttn(self.fenetre,750,1,str(self.win),"#eeeeee","#000000")



def main():
    """
    Création de la première fenêtre des choix des menus
    """
    #####################CONFIGURATION#########################
    global screen
    screen = Tk()
    screen.geometry('5x111')
    screen.configure(bg="#141414")
    #####################BOUTONS#########################
    bttn(screen,0,0,"LANCER","#ffcc66","#141414",launch)
    bttn(screen,0,37,"SURVIE","#ffcc66","#141414",launchS)
    bttn(screen,0,74,"QUITTER","#f86263","#141414",screen.destroy)
    ##############################################
    screen.mainloop()



def launch():
    screen.destroy()
    game()

def launchS():
    screen.destroy()
    game(1)
  
main()