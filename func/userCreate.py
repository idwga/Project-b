import os


class run():
    print("\n")


    if os.path.exists("data/record/user"):
        print("[user] yes")
    else:
        ir = open("data/record/userDev", "r")
        user = ir.read()
        ir.close()
        ua = open("data/record.user", "a")
        for a in user:
            ua.write(a)
        ua.close()
