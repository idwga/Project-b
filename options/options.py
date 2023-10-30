from func import name

class run:
    print("")

    print('what would you like to do today')
    a=0
    b=0
    while a==0:
        ia = open("data/display/options{index}".format(index=b))
        print(ia.read())
        ia.close()
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

        if(inp=="d"):
            from func import web
            web.run()

        

        if(inp=="p"):
            b-=1
        if(inp=="n"):
            b+=1
        if(inp=="q"):
            print("\nQuitting....")
            a=1
        print("-----------------------------------------")
        print("\n\n")

