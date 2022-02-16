import tkinter

def label(W,texte,bcolor,fcolor):

    def on_enter(e):
        label['background']=fcolor
        label['foreground']=bcolor

    def on_leave(e):
        label['background'] = bcolor
        label['foreground'] = fcolor

    label = tkinter.Label(
    W,
    text = texte,
    font=("Helvetica", 14),
    bg=bcolor,
    fg = fcolor,
    activeforeground=fcolor,
    activebackground=bcolor)

    label.bind("<Enter>",on_enter)
    label.bind("<Leave>",on_leave)

    label.pack(ipadx=10, ipady=10)

    return label