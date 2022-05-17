import tkinter
import random
import pyttsx3
import json


############################################################################
################################### INPUT ##################################
############################################################################

def bttn(W,x,y,text,bcolor,fcolor,cmd=None):
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
	mybutton=tkinter.Button(W,width=42,height=2,text=text,
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


def label(W,texte,bcolor,fcolor):
	label = tkinter.Label(
    W,
    text=texte,
    font=("Helvetica", 14),
    bg=bcolor,
    fg = fcolor)

	label.pack(ipadx=10, ipady=10)

############################################################################
################################### DATA ###################################
############################################################################

def import_data(url):
	"""
	get data
	input : url (str)
	output : data (list 2d)
	"""
	with open(url) as read_file:
		data = json.load(read_file)
	return data

def give_data(url,data):
	"""
	remplace un fichier json par une nouvelle valeur
	"""
	with open(url,"w") as fp:
		json.dump(data,fp)


############################################################################
################################### QUESTION ###############################
############################################################################

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
		return self.data[len(import_data('data/score.json'))]

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
		self.url = 'assets/images/'+str(self.take_len())+'.gif'
		label(self.screen,question,"#1FCCD1","#141414")
		self.talk(self.list_question[0])
		self.picture()
		bttn(self.screen,0,0,str(len(self.list_answers)+1)+"/"+str(len(import_data('data/questions.json'))+1),"#141414","#1FCCD1")
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

	def end_game(self):
		"""
		verifie si toutes les questoins ont été repondu pour pouvoir afficher le score et le stoquer dans un fichier de mémoires
		"""
		if len(import_data('data/score.json')) >= len(import_data('data/questions.json'))+1:
			false = 0
			true = 0
			for i in import_data('data/score.json'):
				if i == False:
					false += 1
				else:
					true += 1
			print("vous avez eu {} bonne réponse sur {}\n".format(true,true+false))
			print("solution : \n")
			list_question = import_data('data/questions.json')
			for i in range(len(list_question)):
				print("Question {} : {} \n Réponse: {}\n".format(i,list_question[i][0],list_question[i][list_question[i][-1]+1]))	
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
		if self.end_game() == False:
			questionnaire()

	def picture(self):
		self.img = tkinter.PhotoImage(file=self.url)
		self.image = tkinter.Label(image=self.img).pack()



############################################################################
################################### MAIN ###################################
############################################################################


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
	give_data('data/score.json',[])
	screen.destroy()
	questionnaire()

main()