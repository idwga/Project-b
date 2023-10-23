class main:
    print("Would you like to begin?(y/n)\n")
    inp = input()
    if(inp=="dev"):
        from head import dmod
        dmod.run()
    if(inp=="y"):
        from head import main
        main.run()

