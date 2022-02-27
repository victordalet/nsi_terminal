from PIL import Image


def load_image(url):
	with Image.open(url) as image:
		image = image.resize((500,500))
	return image



def traitement(image):
    ascii_char = ' .:-=+*#%@'
    for y in range(image.height):
        line = ""
        for x in range(image.width):
            # on récupère le pixel sous format RGB
            rgb = image.getpixel((x, y))
            # on fait la moyenne de chaque channel pour faire une nuance de gris
            grey = sum(rgb) // len(rgb)
            # on fait un produit en croix pour récupérer l'index
            index = grey * 9 // 255
            # on rajoute 2 espaces, car en console la hauteur d'un char est plus grande que sa largeur
            line += ascii_char[index] + "  "
        print(line)


def main():
    traitement(load_image("joconde.jpg"))

main()