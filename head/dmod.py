import os


class run:
    print("[DEV-MODE ACTIVATED]\n")
    b = 0
    while b < 1:
        a = input("<Project-B-Devmode>:~")
        
        if (a == "1"):
            from func import logCreate
            logCreate.run()
        if (a == "2"):
            from func import logCreate
            from start import intro
            from func import userCreate
            from options import options
            userCreate.run()
            intro.run()
            print("\n")
            options.run()
        if (a=="imgScr"):
            from scraping import imgScraper
            imgScraper.run()
        if  (a=="util"):
            from options import optionsU
            optionsU.run()
        if (a == "h"):
            ir = open("data/display/bypassCode", "r")
            mes = ir.read()
            ir.close()
            print(mes)
        if (a == "q"):
            if os.path.exists("data/record/log"):
                from func import clearTempCache
                clearTempCache.run()
            b += 1
