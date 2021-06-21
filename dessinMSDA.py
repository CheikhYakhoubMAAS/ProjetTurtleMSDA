'''Module qui permet de dessiner.'''
import turtle
import math
def dessin_carre(taille,couleur):
    '''Permet de dessiner un carré
     de taille et de couleur.'''
    
    turtle.color(couleur)
    turtle.title("Dessiner un carré")
    turtle.bgcolor("light blue")
    turtle.width(3)
    for i in range(4):
        turtle.forward(taille)
        turtle.left(90)
    
    
def dessin_rectangle(largeur,longueur,couleur):
    '''Permet de dessiner un rectangle
     de longeur L, de largeur l et de couleur. '''
    
    turtle.color(couleur)
    turtle.title("Dessiner un rectangle")
    turtle.bgcolor("light blue")
    turtle.width(3)
   
    for i in range(2):
        turtle.forward(largeur) # Déplace la tortue de 150 unités vers l'avant
        turtle.left(90) # rotation de la tortue de 90 degrés
        turtle.forward(longueur) # Déplace la tortue de 80 unités vers l'avant
        turtle.left(90) # rotation de la tortue de 90 degrés
    
def dessin_parallelogramme(taille1,taille2,angle,couleur):
    ''' Permet de dessiner un parallelogramme de taille,d'angle et de couleur '''
    
    turtle.color(couleur)
    turtle.title("Dessiner un losange")
    turtle.bgcolor("light blue")
    turtle.width(3)
    c=0
    while c<4:
        if (c%2==0):
            turtle.left(angle)
            turtle.forward(taille1)
    
        if (c%2==1):
            turtle.left(180-angle)
            turtle.forward(taille2)
        c+=1

def dessin_triangle_equilateral(c,couleur):
    '''Permet de dessiner un triangle équilatéral.'''
    turtle.width(3)
    turtle.color(couleur)
    turtle.bgcolor("light blue")
    for i in range(3):
        turtle.forward(c) 
        turtle.left(120)

def dessin_triangle(taille,couleur):
    ''''Permet de dessiner un triangle de taille et de couleur'''
    
    turtle.color(couleur)
    turtle.title("Dessiner un triangle")
    turtle.bgcolor("light blue")
    turtle.width(3)
    for i in range(3):
        turtle.forward(taille)
        turtle.left(360/3)

def dessin_triangle_rectangle(taille,couleur):
    ''''Permet de dessiner un triangle rectangle de taille et de couleur'''
    
    turtle.color(couleur)
    turtle.title("Dessiner un triangle")
    turtle.bgcolor("light blue")
    turtle.width(3)
    turtle.forward(taille)
    turtle.left(135)
    turtle.forward(taille/math.sqrt(2))
    turtle.left(90)
    turtle.forward(taille/math.sqrt(2))
    turtle.left(135)
    
    
def dessin_cercle(r,couleur):
    '''Permet de dessiner un cercle de rayon r'''
    
    turtle.color(couleur)
    turtle.title("Dessiner un cercle")
    turtle.bgcolor("light blue")
    turtle.width(3)
    turtle.circle(r)     
       
def dessin_demi_cercle(r,couleur):
    '''Permet de dessiner un demi cercle de rayon r'''
    
    turtle.title("Dessiner un cercle")
    turtle.bgcolor("light blue")
    turtle.up()
    turtle.goto(0,-r)
    turtle.down()
    turtle.width(3)
    turtle.circle(r,180)
    
def dessin_polygone_parametrable(cote,taille):
    '''Dessiner un polygone'''
    tur = turtle.Turtle()
    turtle.title("Dessiner un polygone")
    turtle.bgcolor("light blue")
    tur.color("red")
    tur.width(3)
    for i in range(cote):
        tur.forward(taille)
        tur.left(360/cote)
        
def dessin_losange(taille,angle,couleur):
    ''' Permet de dessiner un losange de taille,d'angle et de couleur '''
    tur = turtle.Turtle()
    tur.color(couleur)
    turtle.title("Dessiner un losange")
    turtle.bgcolor("light blue")
    tur.width(3)
    c=0
    while c<4:
        if (c%2==0):
            tur.right(angle)
            tur.forward(taille)
    
        if (c%2==1):
            tur.right(180-angle)
            tur.forward(taille)
        c+=1
def dessin_trapeze(B,b,h):
    t = turtle.Turtle()
    t.forward(B)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(b)
    t.left(45)
    t.forward(B/2)
    t.left(90)     

def dessin_ellipse(rad,couleur):
    '''Permet de dessiner une ellipse'''
   
    turtle.bgcolor('light blue')
    turtle.title("Dessiner une ellipse")
    turtle.seth(-10)
    turtle.color(couleur)
    turtle.width(2) 
    for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)
