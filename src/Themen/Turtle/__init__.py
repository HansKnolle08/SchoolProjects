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

    Parameter:
    - speed: int -> Bestimmt die Geschwindigkeit des Stiftes
    - shape: str -> Bestimmt das Aussehen des Stiftes
    - pensize: int -> Bestimmt die Größe des Stiftes
        - Standard Wert: 1
    - color: str -> Bestimmt die Farbe des Stiftes
        - Standard Wert: Schwarz
    - debug_multipilier: float -> Zum debugging um den Code schneller laufen zu lassen
        - Standard Wert: 1.0
    - window_width: int -> Bestimmt die Breite des Fensters
        - Standard Wert: 800
    - window_height -> Bestimmt die Höhe des Fensters
        - Standard Wert: 800
    """