import tkinter
from py.input import * 
from py.data import *
from py.load import *

def main():
	"""
	Création de la première fenêtre des choix des menus
	"""
	#####################CONFIGURATION#########################
	global screen
	screen = tkinter.Tk()
	screen.geometry('300x74')
	screen.title("CODE DE LA ROUTE")
	screen.configure(bg="#141414")
	#####################BOUTONS#########################
	bttn(screen,0,0,"LANCER","#ffcc66","#141414",launch)
	bttn(screen,0,37,"QUITTER","#f86263","#141414",screen.destroy)
	##############################################
	screen.mainloop()



def launch():
	screen.destroy()
	questionnaire()

main()