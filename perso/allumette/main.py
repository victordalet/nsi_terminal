import tkinter
from py.button import *
from py.screen import *


def main():
	global screen
	screen = tkinter.Tk()
	screen.geometry('300x110')
	screen.title("ALLUMETTE")
	screen.configure(bg="#141414")
	bttn(screen,42,"FACILE","#ffcc66","#141414",launch)
	bttn(screen,42,"DIFFICILE","#25dae9","#141414")
	bttn(screen,42,"QUITTER","#f86263","#141414",screen.destroy)
	screen.mainloop()



def launch():
	screen.destroy()
	run = Game()
	
main()