from tkinter import *

def bttn(W,x,y,text,bcolor,fcolor,cmd=None,w=5,h=2):
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
    mybutton=Button(W,width=w,height=h,text=text,
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

def label(W,x,y,text,bcolor,fcolor):
    mylabel = Label(W,width=5,height=2,text=text,fg=bcolor,bg=fcolor,border=0)
    mylabel.place(x=x,y=y)
    return mylabel
