class run:
    import os
    if os.path.exists("data/record/user"):
        os.remove("data/record/user")
    else:
        print("Error:Temporary Cache does not exist") 
    