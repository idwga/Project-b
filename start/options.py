import os
from asset import name

class run:
    print("")

print('what would you like to do today')
print(name.run())

a=0
while a==0:
    inp = input("[a]Read log          [b]Run a message\n[c]Read Message     [q]Quit\n")   
    if(inp=="a"):
        print("\n\nLog is logged as follow\n------------------------\n")
        ir = open("data/log.txt", "r")
        mes = ir.read()
        ir.close()
        print(mes)
    if(inp=="c"):
        if os.path.exists("data/log.txt"):
            os.remove("data/log.txt")
    if(inp == "b"):
        ir = open("data/message.txt", "r")
        mes = ir.read()
        ir.close()
        print(mes)
    if(inp=="q"):
        print("Quitting....")
        a=1
    print("\n\n")

