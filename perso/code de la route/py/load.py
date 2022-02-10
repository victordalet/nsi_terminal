import tkinter
from py.data import *
from py.input import *
import random
import pyttsx3



class questionnaire:

	def __init__(self):
		self.screen = tkinter.Tk()
		self.screen.geometry(str(self.screen.winfo_screenwidth())+'x'+str(self.screen.winfo_screenheight()))
		self.screen.title("CODE DE LA ROUTE")
		self.screen.configure(bg="#141414")
		self.data = import_data('data/questions.json')
		self.list_question = self.random_question()
		self.display()
		self.screen.mainloop()
		self.list_answers = []

	def random_question(self):
		return random.choice(self.data)

	def display(self):
		question = self.list_question[0]
		choice1 = self.list_question[1]
		choice2 = self.list_question[2]
		choice3 = self.list_question[3]
		choice4 = self.list_question[4]
		good = self.list_question[5]
		url_image = 'assets/images/'+str(self.take_len())+'.png'
		label(self.screen,question,"#d5d5d5","#f86263")
		self.talk(self.list_question[0])
		#picture(W,url_image)
		bttn(self.screen,self.screen.winfo_screenwidth()*1/5,self.screen.winfo_screenheight()*2/3,choice1,"#d5d5d5","#f86263",self.valide1)
		bttn(self.screen,self.screen.winfo_screenwidth()*3/5,self.screen.winfo_screenheight()*2/3,choice2,"#d5d5d5","#f86263",self.valide2)
		bttn(self.screen,self.screen.winfo_screenwidth()*1/5,self.screen.winfo_screenheight()*3/4,choice3,"#d5d5d5","#f86263",self.valide3)
		bttn(self.screen,self.screen.winfo_screenwidth()*3/5,self.screen.winfo_screenheight()*3/4,choice4,"#d5d5d5","#f86263",self.valide4)



	def take_len(self):
		for i in range(len(self.data)):
			if self.data[i] == self.list_question:
				self.del_question(self.data[i])
				return i+1

	def del_question(self,rang):
		new_list = []
		for i in self.data:
			if i != rang:
				new_list += i
		self.data = new_list

	def talk(self,text):  
		s = pyttsx3.init()    
		s.say(text)  
		s.runAndWait() 

	def valide1(self):
		reponse = import_data('data/questions.json')[-1]
		self.end_game(reponse)
		if reponse == 1:
			self.list_answers += True
		else : 
			self.list_answers += False
		self.new_question()

	def valide2(self):
		reponse = import_data('data/questions.json')[-1]
		self.end_game(reponse)
		if reponse == 2:
			self.list_answers += True
		else : 
			self.list_answers += False
		self.new_question()

	def valide3(self):
		reponse = import_data('data/questions.json')[-1]
		self.end_game(reponse)
		if reponse == 3:
			self.list_answers += True
		else : 
			self.list_answers += False
		self.new_question()

	def valide4(self):
		reponse = import_data('data/questions.json')[-1]
		self.end_game(reponse)
		if reponse == 4:
			self.list_answers += True
		else : 
			self.list_answers += False
		self.new_question()

	def end_game(self,list):
		if len(list) == 39:
			for i in range(len(self.list_answers)):
				print("questions {} la réponse étais {}".format(i+1, self.list_answers[i]))
			list_score = import_data('data/score.json')	
			list_score += [self.list_answers]
			give_data('data/score.json',list_score)

