from tkinter import *
from input import * 
from data import *
import random
import time

class game:
    def __init__(self,mode=0):
        self.screen=Tk()
        self.Fond=Canvas(self.screen,bg='white',width=800,height=600)
        self.photoballe = []
        for i in range (2,7):
            self.photoballe.append(PhotoImage(file='boule'+str(2**i)+'.gif')) # stockage image
        self.balle = [
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for i in range(3):
            ############## Remplissage donnée ###############
            self.balle[0].append(random.randint(50,450))
            self.balle[1].append(-100)
            self.balle[2].append(random.randint(2,6))
            self.balle[3].append((-1)**random.randint(1,2)*random.randint(1,5))
            self.balle[4].append(random.randint(1,6))
            self.balle[5].append(self.Fond.create_image(self.balle[0][i],self.balle[1][i],image=self.photoballe[self.balle[2][i]-2]))
        self.position = 300 # position du joeur
        self.vitesse = 20 # vitesse du joeur
        self.win = 3 # nombre de vie
        self.mode = mode # mode de jeu
        self.droit = True # pour le collisions du murs
        self.gauche = True # pour le collisions du murs
        self.pause = False # si le jeu est en pause ou non
        self.time_d = round(time.time()) # le temps de dépard du chrono
        self.time_pause = 0  # afin de soustraire le temps lorsque le jeu est en pause
        self.spon_bonus = False # pour faire spon un bonus
        self.time_max_bonus = 5 # temps max pour le bonus
        self.time_pause_bonus = 0# temps pause lors bonus active
        self.random_spon_bonus = 0 # pour le x du bonus
        self.position_bonus = 0 # pour le y du bonus
        self.petite_taille = 0 # pour aligner le pn lors du bonus

        self.screen.bind('<Right>', self.xmore)
        self.screen.bind('<Left>',self.xless)

        self.display() # on affiche les premiers éléments
        self.Fond.grid()
        self.animation() #le jeu ce déroule dans cette fonction
        self.screen.mainloop()

    def xmore(self,event=None):  
        if self.win != False and self.pause != True:
            if self.droit:
                self.Fond.delete(self.image)
                self.position += self.vitesse
                if self.spon_bonus != 2:
                    self.picture_pn("NoelD.gif")
                else:
                    self.picture_pn("NoelDb.gif")
        
    def xless(self,event=None):
        if self.win != False and self.pause != True:
            if self.gauche:
                self.Fond.delete(self.image)
                self.position -= self.vitesse
                if self.spon_bonus != 2:
                    self.picture_pn("NoelG.gif")
                else:
                    self.picture_pn("NoelGb.gif")

    def wall(self):
        """
        On empeche le perso de sortir de l'écrant en bloquant les commandes
        """
        if self.air_pn()[0] <= 0:
            self.gauche = False
        else: 
            self.gauche = True
        if self.air_pn()[1] >= 850:
            self.droit = False
        else:
            self.droit = True 

    def animation(self):
        """
        on anime les boules et lances les fonctions qui se répètent
        """
        i=0
        while i<len(self.balle[5]) and self.win != False and self.pause != True:
            #################### REBON BALLE #######################
            self.despon=False 
            self.new_x=self.balle[0][i]+self.balle[3][i]
            if self.new_x > 800-2**self.balle[2][i] or self.new_x < 2**self.balle[2][i]:
                self.balle[3][i] = -self.balle[3][i]
                self.new_x=self.balle[0][i]+self.balle[3][i]

            self.new_y = self.balle[1][i]+self.balle[4][i]
            if self.new_y < 2**self.balle[2][i] and self.balle[4][i] < 0 :
                self.balle[4][i]=-self.balle[4][i]
                self.new_y=self.balle[1][i]+self.balle[4][i]

            if self.new_y>600-2**self.balle[2][i]:
                self.balle[4][i]=-self.balle[4][i]
                self.new_y=self.balle[1][i]+self.balle[4][i]
                self.balle[2][i]=self.balle[2][i]-1

                if self.balle[2][i]>=2:
                    self.Fond.itemconfig(self.balle[5][i],image=self.photoballe[self.balle[2][i]-2])
                    self.new_y=self.new_y+2**self.balle[2][i]

                else:
                    self.del_balle(i)
            ################## ACTUALISE COORDONE BALLE #######################        
            if not self.despon: 
                self.balle[0][i],self.balle[1][i] = self.new_x,self.new_y
                self.Fond.coords(self.balle[5][i],self.balle[0][i],self.balle[1][i])
                self.game_over(i)
                i+=1
        #################### AJOUT NOUVELLE BALLE ########################        
        n=len(self.balle[5])
        if n<10:
            self.balle[0].append(random.randint(50,450))
            self.balle[1].append(-100)
            self.balle[2].append(random.randint(2,6))
            self.balle[3].append((-1)**random.randint(1,2)*random.randint(1,5))
            self.balle[4].append(random.randint(1,6))
            self.balle[5].append(self.Fond.create_image(self.balle[0][i],self.balle[1][i],image=self.photoballe[self.balle[2][i]-2]))

        #################### ACTU ET AUTRES FT ########################      
        if self.win != False and self.pause != True:
            self.wall()
            self.ft_spon_bonus()
            self.bonus_active()
        self.time()
        self.screen.after(50,self.animation)

    def del_balle(self,i):
        """
        suppression de la balle, de ses coordonnée, ...
        """
        self.Fond.delete(self.balle[5][i])
        self.balle[0].pop(i)
        self.balle[1].pop(i)
        self.balle[2].pop(i)
        self.balle[3].pop(i)
        self.balle[4].pop(i)
        self.balle[5].pop(i)   
        self.despon=True

    def picture_pn(self,url):
        """
        affiche la photo du père noel selon son sa direction
        """
        self.img = PhotoImage(file=url)
        self.image=self.Fond.create_image(self.position, 525+self.petite_taille, image=self.img)
        

    def air_boule(self,i):
        """
        renvoie les extrémité de la boule
        """
        return self.balle[0][i]-self.balle[2][i],self.balle[0][i]+self.balle[2][i],self.balle[1][i]-self.balle[2][i],self.balle[1][i]+self.balle[2][i]

    def air_pn(self):
        """
        renvoie les extrémité du père noel
        """
        if self.spon_bonus != 2:
            return self.position,self.position+88,450,600
        return self.position,self.position+44,525,600

    def air_bonus(self):
        return self.random_spon_bonus,self.random_spon_bonus+30,self.position_bonus,self.position_bonus+30

    def collision(self,i):
        """
        vérifie les collision entre le père noel et une boulle
        """
        if (self.air_pn()[0] <= self.air_boule(i)[0] <= self.air_pn()[1] or self.air_pn()[0] <= self.air_boule(i)[1] <= self.air_pn()[1]) and (self.air_pn()[2] <= self.air_boule(i)[2] <= self.air_pn()[3] or self.air_pn()[2] <= self.air_boule(i)[3] <= self.air_pn()[3]):
            return 1
        return 0

    def collision_bonus(self):
        """
        vérifie les collision entre le père noel et le bonus
        """
        if (self.air_pn()[0] <= self.air_bonus()[0] <= self.air_pn()[1] or self.air_pn()[0] <= self.air_bonus()[1] <= self.air_pn()[1]) and (self.air_pn()[2] <= self.air_bonus()[2] <= self.air_pn()[3] or self.air_pn()[2] <= self.air_bonus()[3] <= self.air_pn()[3]):
            return True
        return False

    def game_over(self,i): 
        """
        enlève une vie si le père noel est toucher
        """
        test = self.collision(i)
        self.win -= test
        self.del_heart()
        if test:
            self.del_balle(i)
        if self.win == False:
            self.btn_retry = bttn(self.screen,400,300,"retry","#eeeeee","#000000",self.retry)
            if self.mode:
                ############### SAUVEGARDE TU TEMPS RECORDS ################
                if round(time.time())-self.time_d > import_data('score.json'):
                    give_data('score.json',round(time.time())-self.time_d)


    def retry(self):
        """
        relance le jeu
        """
        self.btn_retry.destroy()
        self.screen.destroy()
        if self.mode: game(1)
        else: game()

    def time(self):
        """
        actualise le temps différemment selon les différents mode
        """
        if self.win != False and self.pause != True:
            if self.mode:
                self.btn_time = label(self.screen,35,1,str(round(time.time())-self.time_d-self.time_pause),"#000000","#ffffff")
            else:
                self.btn_time = label(self.screen,35,1,str(60-(round(time.time())-self.time_d-self.time_pause)),"#000000","#ffffff")
                if (60+self.time_pause)-(round(time.time())-self.time_d) <= 0:
                    self.btn_retry = bttn(self.screen,400,300,"retry","#eeeeee","#000000",self.retry)
                    bttn(self.screen,400,330,"Gagné","#eeeeee","#000000")
                    self.win = False
        if self.pause:
            self.time_pause = round(time.time())-self.pause_d
            if self.spon_bonus == 2:
                self.time_pause_bonus = round(time.time()) - self.pause_d_bonus


    def display(self):
        """
        Affichage éléments base
        """
        if self.mode: 
            self.btn_time = label(self.screen,35,1,str(round(time.time())-self.time_d-self.time_pause),"#000000","#ffffff")
            label(self.screen,110,1,str(import_data('score.json')),"#000000","#ffffff")
            self.img_trophee = PhotoImage(file="trophee.gif")
            self.image_trophee = Label(image=self.img_trophee)
            self.image_trophee.place(x=80,y=1)
        else : self.btn_time = label(self.screen,35,1,str(60-(round(time.time())-self.time_d-self.time_pause)),"#000000","#ffffff")
        self.picture_pn('NoelG.gif')
        bttn(self.screen,800/2-40,20,"<","#eeeeee","#000000",self.xless)
        bttn(self.screen,800/2+25,20,">","#eeeeee","#000000",self.xmore)
        self.img_time = PhotoImage(file="time.gif")
        self.image_time = Label(image=self.img_time)
        self.image_time.place(x=1,y=1)
        self.img_h1 = PhotoImage(file="heart.gif")
        self.image_h1 = Label(image=self.img_h1)
        self.image_h1.place(x=710,y=1)
        self.img_h2 = PhotoImage(file="heart.gif")
        self.image_h2 = Label(image=self.img_h2)
        self.image_h2.place(x=740,y=1)
        self.img_h3 = PhotoImage(file="heart.gif")
        self.image_h3 = Label(image=self.img_h3)
        self.image_h3.place(x=770,y=1)
        self.img_pause = PhotoImage(file="pause.gif")
        self.image_pause = Button(image=self.img_pause,command=self.pauseOrPlay)
        self.image_pause.place(x=1,y=32)

    def del_heart(self):
        """
        supprime les coeurs à chaque fois que l'on perds une vie
        """
        if self.win==2:
            self.image_h3.destroy()
        if self .win==1:
            self.image_h2.destroy()
        if self.win==0:
                self.image_h1.destroy() 

    def pauseOrPlay(self):
        """
        met ou non le jeu en pause
        """
        if self.pause == False:
            self.pause = True
            self.img_pause = PhotoImage(file="play.gif")
            self.image_pause = Button(image=self.img_pause,command=self.pauseOrPlay)
            self.image_pause.place(x=1,y=32)
            self.pause_d = round(time.time())-self.time_pause
            self.pause_d_bonus = round(time.time())-self.time_pause_bonus
        else:
            self.pause = False
            self.img_pause = PhotoImage(file="pause.gif")
            self.image_pause = Button(image=self.img_pause,command=self.pauseOrPlay)
            self.image_pause.place(x=1,y=32)

    def ft_spon_bonus(self):
        """
        lance le champi
        """
        if self.spon_bonus == False:
            if random.randint(1,100) <= 1:
                self.spon_bonus = True
                self.random_spon_bonus = random.randint(1,800)
                self.position_bonus = 0
                self.vitesse_bonus = random.randint(1,10)
                self.img_bonus = PhotoImage(file="champi.gif")
                self.image_bonus =self.Fond.create_image(self.random_spon_bonus, self.position_bonus, image=self.img_bonus)
        if self.spon_bonus == True :
            self.position_bonus += self.vitesse_bonus
            self.Fond.delete(self.image_bonus)
            self.image_bonus =self.Fond.create_image(self.random_spon_bonus, self.position_bonus, image=self.img_bonus)
            if self.position_bonus >= 600 : 
                self.Fond.delete(self.image_bonus)
                self.position_bonus = 0
                self.spon_bonus = False



    def bonus_active(self):
        """
        active et désactive le bonus selon le temps
        """
        if self.collision_bonus():
            self.spon_bonus = 2
            self.time_d_bonus = round(time.time())
            self.Fond.delete(self.image_bonus)
            self.petite_taille = 42
            self.Fond.delete(self.image)
            self.picture_pn("NoelGb.gif")


        if self.spon_bonus == 2:
            if (self.time_max_bonus+self.time_pause_bonus)-(round(time.time())-self.time_d_bonus) <= 0:
                self.spon_bonus = False
                self.petite_taille = 0



