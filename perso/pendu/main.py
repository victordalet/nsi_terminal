from tkinter import *
from first_menu import * 


def main():
	W = Tk()
	W.geometry('300x110')
	W.title("Jeu du pendu")
	W.configure(bg="#141414")
	menuOne(W)
	W.mainloop()

main()