from func import name

class run:
    print("")

    print('what would you like to do today')
    print(name.run())

    a=0
    while a==0:
        inp = input("[a]Image scraper      [b]read a message\n[c]Utilities         [q]Quit\n")   
        inp = inp.lower()
        print(inp)
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

