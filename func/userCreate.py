import os


class run():
    print("\n")


    if os.path.exists("data/user"):
        print("[user] yes")
    else:
        ir = open("data/userDev", "r")
        user = ir.read()
        ir.close()
        ua = open("data/user", "a")
        for a in user:
            ua.write(a)
        ua.close()
