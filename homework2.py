class chess:
    def __init__(chess, name, colour):
        chess.heroname = name
        chess.hercolour = colour
    def showinfo(chess):
        print(chess.heroname)
        print(chess.hercolour)
x1 = chess("gun","R")
x2 = chess("bishop","B")
x3 = chess("knight","R")

x1.showinfo()
x2.showinfo()
x3.showinfo()