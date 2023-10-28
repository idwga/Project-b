class run:
    import os
    if os.path.exists("data/record/log"):
        os.remove("data/record/log")
    else:
        print("Error:Cache does not exist") 