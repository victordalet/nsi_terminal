import tkinter

def bttn(W,width,text,bcolor,fcolor,cmd=None):

	def on_enter(e):
		mybutton['background']=bcolor
		mybutton['foreground']=fcolor

	def on_leave(e):
		mybutton['background'] = fcolor
		mybutton['foreground'] = bcolor

	mybutton=tkinter.Button(W,width=width,height=2,text=text,
						fg=bcolor,
						bg=fcolor,
						border=0,
						activeforeground=fcolor,
						activebackground=bcolor,
						command=cmd)

	mybutton.bind("<Enter>",on_enter)
	mybutton.bind("<Leave>",on_leave)

	mybutton.pack()

	return mybutton

def input(W,bcolor,fcolor,cmd=None):

    input = tkinter.Entry(
    W,
    font=("Helvetica", 14),
    bg=bcolor,
    fg = fcolor,
    command=cmd)
    input.pack()

    return input