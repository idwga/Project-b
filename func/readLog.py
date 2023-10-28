class run():
    import os
    if os.path.exists("data/record/log"):
        print("\n\nLog is logged as follow\n------------------------\n")
        ir = open("data/record/log", "r")
        mes = ir.read()
        ir.close()
        print(mes)
    else:
        print("log does not exisist")
