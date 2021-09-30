import tkinter


def choice_question(number_of_question,ecran):
    if number_of_question == 1:
        ecran.made_label('La vitesse est limitée à 50km/h, en raison', ecran.width / 2 - (250 / 2), 0, 250, 50)
        ecran.ConstructionButtunRadioTypeQuestion("de l'absence de visibilité A", 'green', "r1",ecran.width / 2 - (250 / 2), 50, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("du rayon de virage B", 'green', "r2", ecran.width / 2 - (250 / 2),95, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("de la proximité de la fôret C", 'red', "r3",ecran.width / 2 - (250 / 2), 140, 250, 45)
    elif number_of_question == 2:
        ecran.made_label('Ce panneau met fin', ecran.width / 2 - (250 / 2), 0, 250, 50)
        ecran.ConstructionButtunRadioTypeQuestion("au précédente limitations de vitesse A", 'green', "r1",ecran.width / 2 - (250 / 2), 50, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("à l'interdiction de dépasser B", 'red', "r2", ecran.width / 2 - (250 / 2),95, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("à l'interdiction de stationner C", 'red', "r3",ecran.width / 2 - (250 / 2), 140, 250, 45)
    elif number_of_question == 3 :
        ecran.made_label("La consommation d'alcool", ecran.width / 2 - (250 / 2), 0, 250, 50)
        ecran.ConstructionButtunRadioTypeQuestion("augmente le temps de réaction A", 'green', "r1",ecran.width / 2 - (250 / 2), 50, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("rétrécit le champ visuel B", 'green', "r2", ecran.width / 2 - (250 / 2),95, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion(",'augmente pas le temps de réaction C", 'red', "r3",ecran.width / 2 - (250 / 2), 140, 250, 45)
    elif number_of_question == 4:
        ecran.made_label("si je n'obéis pas à cet agent, j'encour", ecran.width / 2 - (250 / 2), 0, 250, 50)
        ecran.ConstructionButtunRadioTypeQuestion("Une amende de 3750€", 'green', "r1",ecran.width / 2 - (250 / 2), 50, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("Un gain de temps B", 'green', "r2", ecran.width / 2 - (250 / 2),95, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("Une perte de 6 points C", 'red', "r3",ecran.width / 2 - (250 / 2), 140, 250, 45)
    elif number_of_question == 5 :
        ecran.made_label('Je peux dépasser le véhicule qui me précède', ecran.width / 2 - (250 / 2), 0, 250, 50)
        ecran.ConstructionButtunRadioTypeQuestion("oui A", 'green', "r1",ecran.width / 2 - (250 / 2), 50, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("non", 'red', "r2", ecran.width / 2 - (250 / 2),95, 250, 45)
        ecran.ConstructionButtunRadioTypeQuestion("en fermant les yeux", 'red', "r3",ecran.width / 2 - (250 / 2), 140, 250, 45)