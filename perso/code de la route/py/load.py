import tkinter
from py.data import *
from py.input import *
import random
import pyttsx3
from tkinter import PhotoImage



class questionnaire:

	def __init__(self):
		self.screen = tkinter.Tk()
		self.screen.geometry(str(self.screen.winfo_screenwidth())+'x'+str(self.screen.winfo_screenheight()))
		self.screen.title("CODE DE LA ROUTE")
		self.screen.configure(bg="#141414")
		self.data = import_data('data/questions.json')
		self.list_question = self.random_question()
		self.list_answers = import_data('data/score.json')
		self.display()
		self.screen.mainloop()

	def random_question(self):
		"""
		chosie une question au hazare dans toutes les question du data set
		"""
		return random.choice(self.data)

	def display(self):
		"""
		affiche le page 
		"""
		question = self.list_question[0]
		choice1 = self.list_question[1]
		choice2 = self.list_question[2]
		choice3 = self.list_question[3]
		choice4 = self.list_question[4]
		good = self.list_question[5]
		url_image = 'assets/images/'+str(self.take_len())+'.png'
		label(self.screen,question,"#1FCCD1","#141414")
		self.talk(self.list_question[0])
		picture(self.screen,url_image)
		bttn(self.screen,0,0,str(len(self.list_answers)+1)+"/40","#141414","#1FCCD1")
		bttn(self.screen,self.screen.winfo_screenwidth()-300,0,"code de la route","#141414","#1FCCD1")
		bttn(self.screen,self.screen.winfo_screenwidth()*1/5,self.screen.winfo_screenheight()*2/3,choice1,"#d5d5d5","#f86263",self.valide1)
		bttn(self.screen,self.screen.winfo_screenwidth()*3/5,self.screen.winfo_screenheight()*2/3,choice2,"#d5d5d5","#f86263",self.valide2)
		bttn(self.screen,self.screen.winfo_screenwidth()*1/5,self.screen.winfo_screenheight()*3/4,choice3,"#d5d5d5","#f86263",self.valide3)
		bttn(self.screen,self.screen.winfo_screenwidth()*3/5,self.screen.winfo_screenheight()*3/4,choice4,"#d5d5d5","#f86263",self.valide4)


	def take_len(self):
		"""
		renvoie le numéro de la question pour retrouver l'image correspondante (2.png) par comparaison
		"""
		for i in range(len(self.data)):
			if self.data[i] == self.list_question:
				self.del_question(self.data[i])
				return i+1

	def del_question(self,rang):
		"""
		supprimer la question utiliser dans notre copie de dataset pour ne pas retomber dessus
		"""
		new_list = []
		for i in self.data:
			if i != rang:
				new_list.append(i)
		self.data = new_list

	def talk(self,text):  
		"""
		diction
		"""
		s = pyttsx3.init()    
		s.say(text)  
		s.runAndWait() 

	def valide1(self):
		"""
		verifie si le bouton cliquer correspond à la bonne réponse
		"""
		reponse = import_data('data/questions.json')[-1]
		if reponse == 1:
			self.list_answers.append(True)
		else : 
			self.list_answers.append(False)
		self.new_question()

	def valide2(self):
		reponse = import_data('data/questions.json')[-1]
		if reponse == 2:
			self.list_answers.append(True)
		else : 
			self.list_answers.append(False)
		self.new_question()

	def valide3(self):
		reponse = import_data('data/questions.json')[-1]
		if reponse == 3:
			self.list_answers.append(True)
		else : 
			self.list_answers.append(False)
		self.new_question()

	def valide4(self):
		reponse = import_data('data/questions.json')[-1]
		if reponse == 4:
			self.list_answers.append(True)
		else : 
			self.list_answers.append(False)
		self.new_question()

	def end_game(self,list):
		"""
		verifie si toutes les questoins ont été repondu pour pouvoir afficher le score et le stoquer dans un fichier de mémoires
		"""
		if len(list) == 39:
			for i in range(len(self.list_answers)):
				print("questions {} la réponse étais {}".format(i+1, self.list_answers[i]))
			list_score = import_data('data/score.json')	
			list_score += [self.list_answers]
			give_data('data/score.json',[])
			return True
		return False

	def new_question(self):
		"""
		lorsqu'une questoin  à été repondu ont reprend les donnée pour changer les questions
		"""
		reponse = import_data('data/questions.json')[-1]
		give_data('data/score.json',self.list_answers)
		self.screen.destroy()
		if not self.end_game(reponse):
			questionnaire()