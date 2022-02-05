from tkinter import *
from py.input import * 
from py.data import *
from py.load import *

def main():
	W = Tk()
	W.geometry('300x110')
	W.title("CODE DE LA ROUTE")
	W.configure(bg="#141414")
	bttn(W,0,0,"LANCER","#ffcc66","#141414",load)
	bttn(W,0,37,"OPTIONS","#25dae9","#141414")
	bttn(W,0,74,"QUITTER","#f86263","#141414",W.destroy)
	W.mainloop()


main()