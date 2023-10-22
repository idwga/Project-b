class run():
    import os
    if os.path.exists("data/log"):
        print("\n\nLog is logged as follow\n------------------------\n")
        ir = open("data/log", "r")
        mes = ir.read()
        ir.close()
        print(mes)
    else:
        print("log does not exisist")
