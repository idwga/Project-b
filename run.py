print("Would you like to begin?(y/n)\n")
inp = input()
if(inp=="dev"):
    import dmod
    dmod.run()
if(inp=="y"):
    import main
    main.run()

