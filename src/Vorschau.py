from Themen.Turtle.main import Drawing # Hier wird mein Modul importiert

# Hier wird ein Drawing Objekt mit dem Namen Turtle erstellt
Turtle = Drawing(
    speed=0, # Das bestimmt die Geschwindigkeit des Stiftes
    shape='turtle', # Das bestimmt die Form des Stiftes
    window_width=1280, # Das bestimmt die Breite des Fensters
    window_height=720, # Das bestimmt die Höhe des Fensters
    pensize=2, # Das bestimmt die dicke des Stiftes
    color='green', # Das bestimmt die Farbe des Stiftes 
    debug_multiplier=0.01 # Das ist ein Multiplikator der die Geschwindigkeit beeinflusst
    )

def Kreis() -> None:
    Turtle.kreis(
        radius=100 # Bestimmt den Radius des Kreises
        )
    
def Quadrat() -> None:
    Turtle.quadrat(
        länge=100 # Bestimmt die beiden Seitenlängen
    )

def Dreieck() -> None:
    Turtle.dreieck(
        länge=100 # Bestimmt die Seitenlängen des Dreiecks
    )

def Rechteck() -> None:
    Turtle.rechteck(
        länge1=100, # Bestimmt die längere Seitenlänge des Rechtecks
        länge2=50 # Bestimmt die Kürzere Seitenlänge des Rechtecks
    )

def n_Eck() -> None:
    Turtle.n_eck(
        seiten=8, # Bestimmt die Anzahl and Seiten und Ecken
        länge=25 # Bestimmt die Seitenlängen des n-Ecks
    )

def Stern() -> None:
    Turtle.stern(
        länge=100 # Bestimmt die Seitenlängen des Sterns
    )

def Nikolaus() -> None:
    Turtle.nikolaus(
        länge=200 # Bestimmt die Seitenlängen der Formen
    )

def Cool_Shape() -> None:
    Turtle.cool_shape(
        shape='circle', # Bestimmt die Grundform
        mode='limit', # Bestimmt ob endlos oder begrenzt gezeichnet werden soll
        länge=100, # Bestimmt die Seitenlängen des Quadrats oder den Radius der Kreises
        schritte=2 # Bestimmt jeder wie vielte Durchlauf gezeichnet wird
        )
    
def Spirale() -> None:
    Turtle.spiral(
        radius=50 # Bestimmt den Anfangsradius des Kreises
    )

def Treppe() -> None:
    Turtle.treppe(
        länge=25, # Bestimmt die länge der Stufen
        stufen=10 # Bestimmt die Anzahl die Stufen
    )

def main() -> None:
    # Kreis()
    # Quadrat()
    # Dreieck()
    # Rechteck()
    # n_Eck()
    # Stern()
    # Nikolaus()
    # Cool_Shape()
    # Spirale()
    # Treppe()
    return None

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        quit()