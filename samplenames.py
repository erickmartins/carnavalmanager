import random

datadir = "/home/erick/Dropbox/erick/carnavalmanager/data/names"

category = "mestresalas"

samples = 10

firstnames = open(datadir + "/" + category + "first.txt")
lastnames = open(datadir + "/" + category + "last.txt")
stats = open(datadir + "/" + "stats.txt")
st = stats.readlines()
firsts = firstnames.readlines()
lasts = lastnames.readlines()
firstnames.close()
lastnames.close()
stats.close()

for line in st:
    if line.startswith(category):
        prob = line.split(" ")[1]
        prob = float(prob)
        if category == 'bateria':
            mestre = line.split(" ")[3]
            mestre = float(mestre)

# print (mestre)
for i in range(samples):
    r = random.random()
    if r < prob:
        print("".join(random.sample(firsts, 1)).strip("\n"))
    else:
        if category == 'bateria':
            r = random.random()
            if r < mestre:
                firstsample = "Mestre"
            else:
                firstsample = "".join(random.sample(firsts, 1)).strip("\n")
        else:
            firstsample = "".join(random.sample(firsts, 1)).strip("\n")
        # print (firstsample)
        string = firstsample + \
            " " + "".join(random.sample(lasts, 1)).strip("\n")
        print (string)
