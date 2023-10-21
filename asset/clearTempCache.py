class run:
    import os
    if os.path.exists("data/user.txt"):
        os.remove("data/user.txt")
    else:
        print("Error:Temporary Cache does not exist") 