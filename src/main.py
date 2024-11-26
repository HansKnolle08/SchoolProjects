from Themen.Turtle.main import Drawing

def main():
    Turtle = Drawing()
    Turtle.n_eck(20)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Programm beendet")