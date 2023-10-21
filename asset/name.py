class name:
    ir = open("data/user.txt", "r")
    dat = ir.read()
    n1 = dat.find("+")+1
    n2 = dat.find(";")
    name = dat[n1:n2]
    print(name)