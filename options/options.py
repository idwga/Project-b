from func import name

class run:
    print("")

    print('what would you like to do today')
    print(name.run())

    a=0
    while a==0:
        ia = open("data/options")
        print(ia.read())
        inp = input(":")   
        inp = inp.lower()
        if(inp=="a"):
            from scraping import imgScraper
            imgScraper.run()
    
        if(inp == "b"):
            from func import message
            message.read()

        if(inp=="c"):
            from options import optionsU
            optionsU.run()

        if(inp=="q"):
            print("\nQuitting....")
            a=1
        print("-----------------------------------------")
        print("\n\n")

