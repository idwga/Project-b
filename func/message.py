
class read():
    ir = open("data/message", "r")
    mes = ir.read()
    ir.close()
    print(mes)


class write():
    def __init__(self, text):
        ma = open("data/message", "a")
        dat = ma.write(text)
        n1 = dat.find("+")+1
        n2 = dat.find(";")
        thing = dat[n1:n2]
