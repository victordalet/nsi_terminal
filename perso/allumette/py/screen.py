import tkinter, random , time
from py.label import *
from py.button import *


class Game:

	def __init__(self):
		self.screen = tkinter.Tk()
		self.screen.geometry(str(self.screen.winfo_screenwidth())+'x'+str(self.screen.winfo_screenheight()))
		self.screen.title("Allumette")
		self.screen.configure(bg="#141414")
		self.list = [random.randint(0,4) for i in range(random.randint(10,15))]
		print(self.list)
		self.display()
		self.screen.mainloop()
		
	def input_nb(self):
		score = self.validation.get()
		score = int(score)
		if score<=3 and score > 0 :
			self.del_list(score)
			self.print.destroy()
			self.print = label(self.screen,'score : '+str(self.list),"#141414","#25dae9")
			stop = self.win(True)
			if stop != True:
				self.bot()
				self.print.destroy()
				self.print = label(self.screen,'score : '+str(self.list),"#141414","#25dae9")
				self.win(False)
		else : 
			print('Erreur : triche')
			return None

	def del_list(self,score):
		for i in range(score):
			number = random.randint(0,len(self.list))
			new_liste = []
			for j in range(len(self.list)):
				if j != number:
					new_liste.append(j)
			self.list = new_liste
		print(self.list)

	def bot(self):
		score = random.randint(1,3)
		self.del_list(score)

	def win(self,player):
		if len(self.list) == 0:
			self.list = [random.randint(0,4) for i in range(random.randint(10,15))]
			print(self.list)
			if player:
				self.print.destroy()
				self.print = label(self.screen,'Vous avez gagné. Nouvelle liste : '+str(self.list),"#141414","#25dae9")
			else : 
				self.print.destroy()
				self.print = label(self.screen,'Vous avez perdu. Nouvelle liste : '+str(self.list),"#141414","#25dae9")
			return True

	def display(self):
		label(self.screen,"Combien d'allumettes voulez-vous prendre?","#d5d5d5","#f86263")
		self.validation = input(self.screen,"#d5d5d5","#f86263")
		bttn(self.screen,20,"OK","#ffcc66","#141414",self.input_nb)
		self.print = label(self.screen,'score : '+str(self.list),"#141414","#25dae9")

