class main:

    ia = open("data/main")
    print(ia.read()+"\n")
    inp = input("<Project-B-home>:~")
    if(inp=="dev"):
        from head import dmod
        dmod.run()
    if(inp=="start"):
        from head import main
        main.run()

