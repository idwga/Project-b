class run:
    import os
    if os.path.exists("data/user"):
        os.remove("data/user")
    else:
        print("Error:Temporary Cache does not exist") 