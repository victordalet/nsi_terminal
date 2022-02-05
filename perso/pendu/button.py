from tkinter import *



def bttn(W,x,y,text,bcolor,fcolor,cmd):

	def on_enter(e):
		mybutton['background']=bcolor
		mybutton['foreground']=fcolor

	def on_leave(e):
		mybutton['background'] = fcolor
		mybutton['foreground'] = bcolor

	mybutton=Button(W,width=42,height=2,text=text,
						fg=bcolor,
						bg=fcolor,
						border=0,
						activeforeground=fcolor,
						activebackground=bcolor,
						command=cmd)

	mybutton.bind("<Enter>",on_enter)
	mybutton.bind("<Leave>",on_leave)

	mybutton.place(x=x,y=y)