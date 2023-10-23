import os


class run:
    print("\n\n[DEV-MODE ACTIVATED]\n")
    b = 0
    while b < 1:
        a = input(":")
        if (a == "1"):
            from func import logCreate
            logCreate.run()
        if (a == "2"):
            from func import logCreate
            from start import intro
            from func import userCreate
            from start import options
            userCreate.run()
            intro.run()
            print("\n")
            options.run()
        if (a == "h"):
            ir = open("data/bypassCode", "r")
            mes = ir.read()
            ir.close()
            print(mes)
        if (a == "q"):
            if os.path.exists("log/log"):
                from func import clearTempCache
                clearTempCache.run()
            b += 1
