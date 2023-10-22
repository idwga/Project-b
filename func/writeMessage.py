class run():
    print("\n Write your message below:")
    mes = input("")
    ua = open("data/message", "o")
    for a in mes:
        ua.write(a)
    ua.close()