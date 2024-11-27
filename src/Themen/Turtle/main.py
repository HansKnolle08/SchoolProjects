import turtle as t
from time import sleep, time

class Drawing:
    """
    Diese Klasse beinhaltet alle methoden und Funktionen die ich zum Thema "Turtle" gemacht habe.

    Methoden:
    - Kreis(self, radius: int = 50, exitonclick: bool = True) -> None
    - Quadrat(self, länge: int = 100, exitonclick: bool = True) -> None
    - Dreieck(self, länge: int = 100, exitonclick: bool = True) -> None
    - Rechteck(self, länge1: int = 100, länge2: int = 50, exitonclick: bool = True) -> None
    - n_eck(self, seiten: int = 4, länge: int = 50, exitonclick: bool = True) -> None
    - Stern(self, länge: int = 100, exitonclick: bool = True) -> None
    - Nikolaus(self, exitonclick: bool = True) -> None
    """
    def __init__(self, speed: int, shape: str, pensize: str = 1, color: str = "black", debug_multiplier: float = 1.0) -> None:
        self.drawing = t.Turtle()
        self.drawing.speed(speed)
        self.drawing.shape(shape)
        self.drawing.pensize(pensize)
        self.drawing.pencolor(color)
        self.deb_mul = debug_multiplier
        self.n = 0

    @staticmethod
    def execution_time(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            print(f'Die Methode {func.__name__} hatte eine Ausführungszeit von: {end_time - start_time:.6f} seconds')
            return result
        return wrapper
    
    @execution_time
    def Kreis(self, radius: int = 50, exitonclick: bool = True) -> None:
        """
        Zeichnet einen Kreis
        
        Parameter:
        - radius: int -> Bestimmt den Radius des Kreises
            - Standard Wert: 50

        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        self.drawing.circle(radius)
        if exitonclick:
            t.exitonclick()

    @execution_time
    def Quadrat(self, länge: int = 100, exitonclick: bool = True) -> None:
        """
        Zeichnet ein Quadrat
        
        Parameter:
        - länge: int -> Bestimmt die Seitenlängen des Quadrats
            - Standard Wert: 100

        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        i = 0
        while not i == 4:
            self.drawing.forward(länge)
            sleep(1 * self.deb_mul)
            self.drawing.right(90)
            i+=1
        if exitonclick:
            t.exitonclick()

    @execution_time
    def Dreieck(self, länge: int = 100, exitonclick: bool = True) -> None:
        """
        Zeichnet ein Dreieck
        
        Parameter:
        - länge: int -> Bestimmt die Seitenlängen des Dreiecks
            - Standard Wert: 100

        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        i = 0
        while not i == 3:
            self.drawing.forward(länge)
            sleep(1 * self.deb_mul)
            self.drawing.left(120)
            i+=1
            print(i)
        if exitonclick:
            t.exitonclick()

    @execution_time
    def Rechteck(self, länge1: int = 100, länge2: int = 50, exitonclick: bool = True) -> None:
        """
        Zeichnet ein Rechteck
        
        Parameter:
        - länge1: int -> Bestimmt die erste Seitenlänge des Rechtecks
            - Standard Wert: 100
        - länge2: int -> Bestimmt die zweite Seitenlänge des Rechtecks
            - Standard Wert: 50

        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        i = 0
        while not i == 2:
            self.drawing.forward(länge1)
            sleep(1 * self.deb_mul)
            self.drawing.right(90)
            sleep(1 * self.deb_mul)
            self.drawing.forward(länge2)
            sleep(1 * self.deb_mul)
            self.drawing.right(90)
            i+=1
        if exitonclick:
            t.exitonclick()

    @execution_time
    def n_eck(self, seiten: int = 4, länge: int = 50, exitonclick: bool = True) -> None:
        """
        Zeichnet ein n-Eck
        
        Parameter:
        - seiten: int -> Bestimmt die ANzahl an Seiten und Ecken des n-Ecks
            - Standard Wert: 4
        - länge: int -> Bestimmt die Seitenlängen des n-Ecks
            - Standard Wert: 50

        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        i = 0
        while not i == seiten:
            self.drawing.forward(länge)
            sleep(1 * self.deb_mul)
            self.drawing.right(360 / seiten)
            i+=1
        if exitonclick:
            t.exitonclick()

    @execution_time
    def Stern(self, länge: int = 100, exitonclick: bool = True) -> None:
        """
        Zeichnet einen Stern

        Parameter:
        - länge: int -> Bestimmt die Seitenlängen des Sterns
            - Standard Wert: 100

        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        for self.n in range(5):
            self.drawing.forward(länge)
            sleep(1 * self.deb_mul1)
            self.drawing.left(144)
        if exitonclick:
            t.exitonclick()

    @execution_time
    def Nikolaus(self, exitonclick: bool = True) -> None:
        """
        Zeichnet ein Nikolaushaus

        Parameter:
        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        """
        self.Quadrat(exitonclick=False)
        self.Dreieck(exitonclick=False)
        if exitonclick:
            t.exitonclick()
    
    @execution_time
    def cool_shape(self, länge: int = 50, schritte: int = 10, exitonclick: bool = True) -> None:
        """
        Zeichnet eine coole Form

        Parameter:
        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        - länge: int -> Bestimmt die Seitenlängen des Quadrats
            - Standard Wer: 50
        """
        i: int = 0
        if schritte >= 360:
            schritte = 360

        while not i == 360:
            self.drawing.left(i)
            self.Quadrat(länge=länge, exitonclick=False)
            i+=schritte
            print(i)
        if exitonclick:
            t.exitonclick()

def main() -> None:
    """
    Hauptfunktion zum Ausführen und Testen des Modules
    """
    my_funcs = Drawing(speed=0, shape="turtle", pensize=1, color="red", debug_multiplier=0.0001)
    my_funcs.n_Zacken(länge=200, zacken=10)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Programm beendet")
