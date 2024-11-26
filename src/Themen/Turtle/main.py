import turtle as t
import time

class Functions:
    """
    Diese Klasse beinhaltet alle methoden und Funktionen die ich zum Thema "Turtle" gemacht habe.
    """
    def __init__(self) -> None:
        self.hansisi = t.Turtle()
        self.hansisi.speed(0)
        self.hansisi.shape("turtle")

    def Quadrat(self, i: int = 0) -> None:
        while not i == 4:
            self.hansisi.forward(100)
            self.hansisi.right(90)
            i+=1

    def Rechteck(self, i: int = 0) -> None:
        while not i == 2:
            self.hansisi.forward(100)
            self.hansisi.right(90)
            self.hansisi.forward(50)
            self.hansisi.right(90)
            i+=1

    def n_eck(self, i: int = 4) -> None:
        while not i == 100:
            self.hansisi.forward(100)
            self.hansisi.right(360 / i)

    def Stern(self, i: int = 0, n: int = 0) -> None:
        for n in range(5):
            self.hansisi.forward(i)
            time.sleep(1)
            self.hansisi.left(144)

if __name__ == '__main__':
    my_funcs = Functions()
    my_funcs.Stern(300)