import turtle

t = turtle.Turtle()
t.speed(0)


def koch(longueur, n):
    if n == 0:
        t.forward(longueur)
    else:
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)
        t.right(120)
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)

def flocon(taille, etape):
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)


def triangle():
	t.forward(100)
	t.left(120)
	t.forward(100)
	t.left(120)
	t.forward(100)
 
def main():
	print("lancement du programme...")
	t.hideturtle()
	flocon(100,3)
	print("fin du programme")
	turtle.mainloop()

main()