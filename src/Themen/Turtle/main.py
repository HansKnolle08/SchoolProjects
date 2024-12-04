###########
# IMPORTS #
###########
import turtle as t
from time import sleep, time

################################
# DEFINITION OF THE MAIN CLASS #
################################
class Drawing:
    """
    Diese Klasse beinhaltet einige Methoden und Funktionen die ich zum Thema "Turtle" gemacht habe.

    Methoden:
    - Kreis(self, radius: int = 50, exitonclick: bool = True) -> None
    - Quadrat(self, länge: int = 100, exitonclick: bool = True) -> None
    - Dreieck(self, länge: int = 100, exitonclick: bool = True) -> None
    - Rechteck(self, länge1: int = 100, länge2: int = 50, exitonclick: bool = True) -> None
    - n_eck(self, seiten: int = 4, länge: int = 50, exitonclick: bool = True) -> None
    - Stern(self, länge: int = 100, exitonclick: bool = True) -> None
    - Nikolaus(self, länge: int = 100, exitonclick: bool = True) -> None
    - cool_shape(self, shape: str, mode: str = 'limit', länge: int = 50, schritte: int = 10, exitonclick: bool = True) -> None
    - spiral(self, radius: int = 50, exitonclick: bool = True) -> None

    Parameter:
    - speed: int -> Bestimmt die Geschwindigkeit des Stiftes
    - shape: str -> Bestimmt das Aussehen des Stiftes
    - pensize: int -> Bestimmt die Größe des Stiftes
        - Standard Wert: 1
    - color: str -> Bestimmt die Farbe des Stiftes
        - Standard Wert: Schwarz
    - debug_multiplier: float -> Zum debugging um den Code schneller laufen zu lassen
        - Standard Wert: 1.0
    - window_width: int -> Bestimmt die Breite des Fensters
        - Standard Wert: 800
    - window_height -> Bestimmt die Höhe des Fensters
        - Standard Wert: 800
    """
    ###############
    # INITIALIZER #
    ###############
    def __init__(self, speed: int, shape: str, window_width: int = 800, window_height: int = 800, pensize: int = 1, color: str = "black", debug_multiplier: float = 1.0) -> None:

        #################
        # Variable init #
        #################
        self.speed: int = speed
        self.shape: str = shape
        self.pensize: int = pensize
        self.color: str = color
        self.deb_mul: int = debug_multiplier
        self.width: int = window_width
        self.height: int = window_height

        #########################
        # Turtle init and setup #
        #########################
        self.drawing = t.Turtle()
        t.setup(width=self.width, height=self.height)
        self.drawing.speed(self.speed)
        self.drawing.shape(self.shape)
        self.drawing.pensize(self.pensize)
        self.drawing.pencolor(self.color)
        self.drawing.pendown()
        self.n: int = 0

        #############
        # Constants #
        #############
        self.QUADRAT_SHAPE_VARS: list[str] = ['q', 'quadrat', 'qd']
        self.CIRCLE_SHAPE_VARS: list[str] = ['c', 'circle', 'cr']
        self.LIMIT_MODE_VARS: list[str] = ['lim', 'l', 'limited', 'limit']
        self.ENDLESS_MODE_VARS: list[str] = ['end', 'el', 'endless']

        ################
        # Methods init #
        ################
        def __repr__(self) -> str: ...
        def __str__(self) -> str: ...

        def exec_time(func): ...

        def kreis(self, radius: int = 50, exitonclick: bool = True) -> None: ...
        def quadrat(self, länge: int = 100, exitonclick: bool = True) -> None: ...
        def dreieck(self, länge: int = 100, exitonclick: bool = True) -> None: ...
        def rechteck(self, länge1: int = 100, länge2: int = 50, exitonclick: bool = True) -> None: ...
        def n_eck(self, seiten: int = 4, länge: int = 50, exitonclick: bool = True) -> None: ...
        def stern(self, länge: int = 100, exitonclick: bool = True) -> None: ...
        def nikolaus(self, länge: int = 100, exitonclick: bool = True) -> None: ...
        def cool_shape(self, shape: str, mode: str = 'limit', länge: int = 50, schritte: int = 10, exitonclick: bool = True) -> None: ...
        def spiral(self, radius: int = 50, exitonclick: bool = True) -> None: ...

        def main() -> None: ...

    ########################
    # OTHER DUNDER-METHODS #
    ########################
    def __repr__(self) -> str:
        return f'Drawing object with Attributes Speed: {self.speed}, Shape: {self.shape}, Pensize: {self.pensize}, Color: {self.color}, Debug Multiplier: {self.deb_mul}'
    
    def __str__(self) -> str:
        return f'Drawing object with Attributes Speed: {self.speed}, Shape: {self.shape}, Pensize: {self.pensize}, Color: {self.color}, Debug Multiplier: {self.deb_mul}'

    #################
    # OTHER METHODS #
    #################
    @staticmethod
    def exec_time(func):
        """
        Diese Methode ist ein Dekorator die die Ausführungszeit einer Funktion ausgibt
        """
        def wrapper(*args, **kwargs) -> int | float:
            start_time: float = time()
            result = func(*args, **kwargs)
            end_time: float = time()
            print(f'Die Methode {func.__name__} hatte eine Ausführungszeit von: {end_time - start_time:.6f} seconds')
            return result
        return wrapper
    
    ################
    # MAIN METHODS #
    ################
    @exec_time
    def kreis(self, radius: int = 50, exitonclick: bool = True) -> None:
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

    @exec_time
    def quadrat(self, länge: int = 100, exitonclick: bool = True) -> None:
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

    @exec_time
    def dreieck(self, länge: int = 100, exitonclick: bool = True) -> None:
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

    @exec_time
    def rechteck(self, länge1: int = 100, länge2: int = 50, exitonclick: bool = True) -> None:
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

    @exec_time
    def n_eck(self, seiten: int = 4, länge: int = 50, exitonclick: bool = True) -> None:
        """
        Zeichnet ein n-Eck
        
        Parameter:
        - seiten: int -> Bestimmt die Anzahl an Seiten und Ecken des n-Ecks
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

    @exec_time
    def stern(self, länge: int = 100, exitonclick: bool = True) -> None:
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
            sleep(1 * self.deb_mul)
            self.drawing.left(144)
        if exitonclick:
            t.exitonclick()

    @exec_time
    def nikolaus(self, länge: int = 100, exitonclick: bool = True) -> None:
        """
        Zeichnet ein Nikolaushaus

        Parameter:
        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        - länge: int -> Bestimmt die Seitenlängen der Formen
            - Standard Wert: 100
        """
        self.quadrat(länge=länge, exitonclick=False)
        self.dreieck(länge=länge, exitonclick=False)
        if exitonclick:
            t.exitonclick()
    
    @exec_time
    def cool_shape(self, shape: str, mode: str = 'limit', länge: int = 50, schritte: int = 10, exitonclick: bool = True) -> None:
        """
        Zeichnet eine coole Form

        Parameter:
        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        - länge: int -> Bestimmt die Seitenlängen des Quadrats
            - Standard Wert: 50
        - schritte: int -> Bestimmt die Anzahl an Durchläufen
            - Standard Wert: 10
        - shape: str -> Bestimmt die Grundform der coolen Form
        - mode: str -> Bestimmt den Modus der Methode
            - Standard Wert: limit (Empfohlen)
        """
        i: int = 0
        if schritte >= 360:
            schritte = 360

        if mode.lower() in self.LIMIT_MODE_VARS:
            if shape.lower() in self.CIRCLE_SHAPE_VARS:
                while not i == 360:
                    self.drawing.left(i)
                    self.kreis(radius=länge, exitonclick=False)
                    i+=schritte
                    print(i)
            elif shape.lower() in self.QUADRAT_SHAPE_VARS:
                while not i == 360:
                    self.drawing.left(i)
                    self.quadrat(länge=länge, exitonclick=False)
                    i+=schritte
                    print(i)
            else:
                print(f'Die eingegebene Form: {shape} existiert nicht')
        elif mode.lower() in self.ENDLESS_MODE_VARS:
            if shape.lower() in self.CIRCLE_SHAPE_VARS:
                while not i == -1:
                    self.drawing.left(i)
                    self.kreis(radius=länge, exitonclick=False)
                    i+=schritte
                    print(i)
            elif shape.lower() in self.QUADRAT_SHAPE_VARS:
                while not i == -1:
                    self.drawing.left(i)
                    self.quadrat(länge=länge, exitonclick=False)
                    i+=schritte
                    print(i)
            else:
                print(f'Die eingegebene Form: {shape} existiert nicht')

        if exitonclick:
            t.exitonclick()

    @exec_time
    def spiral(self, radius: int = 50, exitonclick: bool = True) -> None:
        """
        Zeichnet eine coole Form

        Parameter:
        - exitonclick: bool -> Bestimmt ob die Methode turtle.exitonclick() aufgerufen werden soll
            - Diese Methode ermöglicht es das dass Fenster nicht sofort geschlossen wird sondern erst wenn der Benutzer ein Mausklick tätigt auf das Fenster
            - Standard Wert: True
        - radius: int -> Bestimmt den Anfangsradius des Kreises
            - Standard Wert: 50
        """
        for i in range(0, 360):
            self.drawing.forward(radius)
            self.drawing.left(i)
        if exitonclick:
            t.exitonclick()

#########################
# PROGRAM MAIN FUNCTION #
#########################
@Drawing.exec_time
def main() -> None:
    """
    Hauptfunktion zum Ausführen und Testen des Modules
    """
    my_funcs = Drawing(speed=0, shape="turtle", pensize=1, color="red", debug_multiplier=0.01, window_height=800, window_width=1000)
    my_funcs.n_eck(seiten=64, länge=15)

###############
# ENTRY POINT #
###############
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print("Programm beendet")
