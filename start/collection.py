from datetime import date


class run:
    print("\n")


name1 = input('Provide your first name\n')
name1.strip()
name2 = input('provide your last name\n')
name2.strip()
fname = name1+" "+name2
age = input('Provide your age\n')
age.strip()
today = date.today()
time = today.strftime("%m/%d/%y")
user = ["-"+time, "+"+name1, ";"+name2, ","+age, "."+fname]
log = [time, name1, name2, age, fname]


ua = open("data/user.txt", "a")
for a in user:
    ua.write(a+"\n")
ua.close()

la = open("data/log.txt", "a")
la.write("+\n")
for b in log:
    la.write(b+"\n")
la.close()
