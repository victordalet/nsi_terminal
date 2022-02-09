from py.data import *  
from py.load import *

list_answers = []

def valide1():
	reponse = import_data('data/questions.json')[-1]
	end_game(reponse)
	if reponse == 1:
		list_answers = import_data('data/score.json')
		list_answers.append(True)
		give_data('data/score.json',list_answers)
	else : 
		list_answers = import_data('data/score.json')
		list_answers.append(False)
		give_data('data/score.json',list_answers)
	new_question()

def valide2():
	reponse = import_data('data/questions.json')[-1]
	end_game(reponse)
	if reponse == 2:
		list_answers = import_data('data/score.json')
		list_answers.append(True)
		give_data('data/score.json',list_answers)
	else : 
		list_answers = import_data('data/score.json')
		list_answers.append(False)
		give_data('data/score.json',list_answers)
	new_question()

def valide3():
	reponse = import_data('data/questions.json')[-1]
	end_game(reponse)
	if reponse == 3:
		list_answers = import_data('data/score.json')
		list_answers.append(True)
		give_data('data/score.json',list_answers)
	else : 
		list_answers = import_data('data/score.json')
		list_answers.append(False)
		give_data('data/score.json',list_answers)
	new_question()

def valide4():
	reponse = import_data('data/questions.json')[-1]
	end_game(reponse)
	if reponse == 4:
		list_answers = import_data('data/score.json')
		list_answers.append(True)
		give_data('data/score.json',list_answers)
	else : 
		list_answers = import_data('data/score.json')
		list_answers.append(False)
		give_data('data/score.json',list_answers)
	new_question()

def end_game(list):
	if len(list) == 39:
		print("fin")
