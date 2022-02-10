import tkinter
from py.input import * 
from py.data import *
from py.load import *

def main():
	screen = tkinter.Tk()
	screen.geometry('300x110')
	screen.title("CODE DE LA ROUTE")
	screen.configure(bg="#141414")
	bttn(screen,0,0,"LANCER","#ffcc66","#141414",questionnaire)
	bttn(screen,0,37,"OPTIONS","#25dae9","#141414")
	bttn(screen,0,74,"QUITTER","#f86263","#141414",screen.destroy)
	screen.mainloop()


main()