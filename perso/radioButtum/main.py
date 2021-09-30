import tkinter
from window import *
from question import *

def main():
    print("lancement...")
    ecran = window()
    ################## CHOIX DES COULEURS ##################
    ecran.made_label('couleur du fond',1340,400,180,20)
    ecran.made_input(1340,420,180,20)
    ecran.made_buttum("Appliquer",1340,440,180,30)
    ecran.ConstructionButtunRadioType1("bleu",1,1340,470,60,45)
    ecran.ConstructionButtunRadioType2("vert", 2,1400,470,60,45)
    ecran.ConstructionButtunRadioType3("rouge",3,1460,470,60,45)
    ################## CREATION DE L'HISTORIQUE ##################
    ecran.made_label('Historique', 1340, 515, 180, 20)
    ecran.ConstructionButtunRadioType4("-1", 4, 1340, 535, 60, 45)
    ecran.ConstructionButtunRadioType5("-2", 5, 1400, 535, 60, 45)
    ecran.ConstructionButtunRadioType6("-3", 6, 1460, 535, 60, 45)
    ##################  AFFICHAGE QUESTION ##################
    choice_question(1,ecran)
    ##################  BOUTON POUR LES DIFFERENTES QUESTIONS ##################
    ecran.ConstructionButtunRadioTypeQuestionChoice("Question 1 ", 1,ecran.width / 2 - (250 / 2)-500, 250, 250, 45)
    ecran.ConstructionButtunRadioTypeQuestionChoice("Question 2 ", 2, ecran.width / 2 - (250 / 2)-250, 250, 250,45)
    ecran.ConstructionButtunRadioTypeQuestionChoice("Question 3 ", 3, ecran.width / 2 - (250 / 2), 250, 250,45)
    ecran.ConstructionButtunRadioTypeQuestionChoice("Question 4 ", 4, ecran.width / 2 - (250 / 2)+250, 250, 250,45)
    ecran.ConstructionButtunRadioTypeQuestionChoice("Question 5 ", 5, ecran.width / 2 - (250 / 2)+500, 250, 250,45)


main()
tkinter.mainloop()