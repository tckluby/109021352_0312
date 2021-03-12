class hero:
    def __init__(self, name, id, attack, speed, hp):
        self.heroname = name
        self.heroid = id
        self.heroattack = attack
        self.herospeed = speed
        self.herohp = hp
    def showinfo(self):
        print(self.heroname)
        print(self.heroid)
        print(self.heroattack)
        print(self.herospeed)
        print(self.herohp)
x1 = hero("ak","051","164","70","450")
x2 = hero("af","052","154","80","455")
x3 = hero("ah","053","112","90","460")

x1.showinfo()
x2.showinfo()
x3.showinfo()