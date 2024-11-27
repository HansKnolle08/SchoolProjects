from Themen.Turtle import main as m

def main():
    Turtle = m.Drawing(speed=0, shape="turtle", pensize=10, color="red", debug_multiplier=0.001)
    Turtle.n_eck(20)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Programm beendet")
        print(e)