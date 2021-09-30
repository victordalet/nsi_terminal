import tkinter

class window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("radiobottum")
        self.window.iconbitmap("assets/logo.ico")
        self.window.config(bg = "#87CEEB")
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry('{}x{}'.format(self.width,self.height))
        self.window.attributes('-fullscreen', True)
        self.rbvar = tkinter.StringVar()
        self.rbvar.set("")
        self.list_color_historical = ["#ff00ff", "#00ffff", "ffff00"]

    ##################  CREATION ZONE DE TEXTE ##################
    def made_label(self,message,x,y,w,h):
        self.text1 = tkinter.Label(self.window, text=message, bg='red')
        self.text1.pack()
        self.text1.place(x=x, y=y, width=w, height=h)

    ##################  CREATION ZONE DE TEXTE ##################
    def made_input(self,x,y,w,h):
        self.input = tkinter.Entry(self.window)
        self.input.pack()
        self.input.place(x=x,y=y,width=w,height=h)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON L'ENTREE DU TEXT ##################
    def color_change_text(self):
        color = self.input.get()
        self.window.config(bg = color)
        self.list_color_historical.append(color)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON LE BOUTON POUR LE BLEU ##################
    def color_change_bleu(self):
        color = '#0000ff'
        self.window.config(bg = color)
        self.list_color_historical.append(color)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON LE BOUTON POUR LE VERT ##################
    def color_change_green(self):
        color = '#ff0000'
        self.window.config(bg = color)
        self.list_color_historical.append(color)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON LE BOUTON POUR LE ROUGE ##################
    def color_change_red(self):
        color = '#00ff00'
        self.window.config(bg = color)
        self.list_color_historical.append(color)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON LE BOUTON D'HISTORIQUE POUR -1 ##################
    def color_change_historical1(self):
        color = self.list_color_historical[-2]
        self.window.config(bg=color)
        self.list_color_historical.append(color)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON LE BOUTON D'HISTORIQUE POUR -2 ##################
    def color_change_historical2(self):
        color = self.list_color_historical[-3]
        self.window.config(bg=color)
        self.list_color_historical.append(color)

    ##################  POUR CHANGER LA COULEUR DU FOND SELON LE BOUTON D'HISTORIQUE POUR -3 ##################
    def color_change_historical3(self):
        color = self.list_color_historical[-4]
        self.window.config(bg=color)
        self.list_color_historical.append(color)

    ##################  POUR CREER UN BOUTON  ##################
    def made_buttum(self,message,x,y,w,h):
        self.button = tkinter.Button(self.window, text=message, command=self.color_change_text)
        self.button.pack()
        self.button.place(x=x, y=y, width=w, height=h)

    ##################  POUR CREER DIFFERENTS BOUTONS RADIO ##################
    def ConstructionButtunRadioType1(self,name,value,x,y,w,h):
        self.checkbox = tkinter.Radiobutton(self.window,cursor="mouse", text=name, variable=self.rbvar, value=value,command= self.color_change_bleu)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)

    def ConstructionButtunRadioType2(self,name,value,x,y,w,h):
        self.checkbox = tkinter.Radiobutton(self.window,cursor="mouse", text=name, variable=self.rbvar, value=value,command= self.color_change_red)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)

    def ConstructionButtunRadioType3(self,name,value,x,y,w,h):
        self.checkbox = tkinter.Radiobutton(self.window,cursor="mouse", text=name, variable=self.rbvar, value=value,command= self.color_change_green)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)

    def ConstructionButtunRadioType4(self,name,value,x,y,w,h):
        self.checkbox = tkinter.Radiobutton(self.window,cursor="mouse", text=name, variable=self.rbvar, value=value,command= self.color_change_historical1)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)

    def ConstructionButtunRadioType5(self,name,value,x,y,w,h):
        self.checkbox = tkinter.Radiobutton(self.window,cursor="mouse", text=name, variable=self.rbvar, value=value,command= self.color_change_historical2)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)

    def ConstructionButtunRadioType6(self, name, value, x, y, w, h):
        self.checkbox = tkinter.Radiobutton(self.window, cursor="mouse", text=name, variable=self.rbvar,value=value, command=self.color_change_historical3)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)

    def ConstructionButtunRadioTypeQuestion(self, name,color, value, x, y, w, h):
        self.checkbox = tkinter.Radiobutton(self.window,selectcolor=color,bg='grey', cursor="mouse", text=name,activeforeground=color, variable=self.rbvar,value=value)
        self.checkbox.pack()
        self.checkbox.place(x=x, y=y, width=w, height=h)


