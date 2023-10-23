from func import name

class run:
    print("")

    print('Welcome to utilities')
    print(name.run())

    a=0
    while a==0:
        inp = input("[a]Read log          [b]read a message\n[c]Clear cache       [d]Write a message\n[q]Quit\n")   
        inp = inp.lower()
        print(inp)
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