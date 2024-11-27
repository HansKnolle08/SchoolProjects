from Themen.Turtle.main import Drawing

def main():
    Turtle = Drawing(speed=0, shape="turtle", pensize=10, color="red")
    Turtle.n_eck(20)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Programm beendet")
        print(e)