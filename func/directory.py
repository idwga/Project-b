class run:
    def __str__(self):
        import os
        cwd = os.getcwd()
        mes = cwd
        ua = open("data/record/currentLocation", "w")
        for a in mes:
            ua.write(a)
        ua.close()
        return mes