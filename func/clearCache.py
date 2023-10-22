class run:
    import os
    if os.path.exists("data/log"):
        os.remove("data/log")
    else:
        print("Error:Cache does not exist") 