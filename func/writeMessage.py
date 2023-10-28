class run():
    print("\n Write your for the next user message below:")
    mes = input("")
    ua = open("data/record/message", "w")
    for a in mes:
        ua.write(a)
    ua.close()
    print("\n the next user will see the message")

