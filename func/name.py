class run:
    def __init__(self):
        ir = open("data/record/user", "r")
        dat = ir.read()
        n1 = dat.find("+")+1
        n2 = dat.find(";")
        thing = dat[n1:n2]
    
        self.thing = thing
    def __str__(self):
        return self.thing