from func import name

class run:
    print("")

    print('Welcome to utilities')
    a=0
    while a==0:
        ia = open("data/display/optionsUtil")
        print(ia.read())
        inp = input(":")   
        inp = inp.lower()
        if(inp=="a"):
            from func import readLog
            readLog.run()
    
        if(inp == "b"):
            from func import message
            message.read()

        if(inp=="c"):
            from func import clearCache
            clearCache.run()

        if(inp=="d"):
            from func import writeMessage
            writeMessage.run()

        if(inp=="q"):
            print("\nQuitting....")
            a=1
        print("-----------------------------------------")
        print("\n\n")