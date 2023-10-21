import os
class run:
    ir = open("data/user.txt", "r")
    dat = ir.read()
    n1 = dat.find("+")+1
    n2 = dat.find(";")
    name = dat[n1:n2]
    print('what would you like to do today '+name)
a=0
while a==0:
    inp = input("[a]Read log      [b]Clear log\n[c]Run a message [q]Quit\n")   
    if(inp=="a"):
        print("\n\nLog is logged as follow\n------------------------\n")
        ir = open("data/log.txt", "r")
        mes = ir.read()
        ir.close()
        print(mes)
    if(inp=="b"):
        if os.path.exists("data/log.txt"):
            os.remove("data/log.txt")
    if(inp == "c"):
        ir = open("data/message.txt", "r")
        mes = ir.read()
        ir.close()
        print(mes)
    if(inp=="q"):
        print("Quitting....")
        a=1
    print("\n\n")

