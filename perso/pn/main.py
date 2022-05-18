from tkinter import*
from game import *  

def main():
    """
    Création de la première fenêtre des choix des menus
    """
    global screen
    screen = Tk()
    screen.geometry('300x111')
    screen.configure(bg="#141414")
    bttn(screen,0,0,"LANCER","#ffcc66","#141414",launch,42)
    bttn(screen,0,37,"SURVIE","#ffcc66","#141414",launchS,42)
    bttn(screen,0,74,"QUITTER","#f86263","#141414",screen.destroy,42)
    screen.mainloop()



def launch():
    """
    lancement en mode normal
    """
    screen.destroy()
    game()

def launchS():
    """
    lancement en mode survit
    """
    screen.destroy()
    game(1)
  
main()