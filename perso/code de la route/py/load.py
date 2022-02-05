from tkinter import *
from py.data import *
from py.input import *
import random
import pyttsx3

def load():
	W = Tk()
	W.geometry(str(W.winfo_screenwidth())+'x'+str(W.winfo_screenheight()))
	W.title("CODE DE LA ROUTE")
	W.configure(bg="#141414")
	data = import_data('data/questions.json')
	list_question = random_quetion(data)
	display(W,list_question,data)
	W.mainloop()


def random_quetion(data):
	return random.choice(data)

def display(W,list_question,data):
	question = list_question[0]
	choice1 = list_question[1]
	choice2 = list_question[2]
	choice3 = list_question[3]
	choice4 = list_question[4]
	good = list_question[5]
	url_image = 'assets/images/'+str(take_len(list_question,data))+'.png'
	label(W,question,"#d5d5d5","#f86263")
	talk(question)
	#picture(W,url_image)
	bttn(W,W.winfo_screenwidth()*1/5,W.winfo_screenheight()*2/3,choice1,"#d5d5d5","#f86263")
	bttn(W,W.winfo_screenwidth()*3/5,W.winfo_screenheight()*2/3,choice2,"#d5d5d5","#f86263")
	bttn(W,W.winfo_screenwidth()*1/5,W.winfo_screenheight()*3/4,choice3,"#d5d5d5","#f86263")
	bttn(W,W.winfo_screenwidth()*3/5,W.winfo_screenheight()*3/4,choice4,"#d5d5d5","#f86263")



def take_len(list_question,data):
	for i in range(len(data)):
		if data[i] == list_question:
			return i+1

def talk(text):  
	s = pyttsx3.init()    
	s.say(text)  
	s.runAndWait() 