import glob
import os

path = '/home/erick/Dropbox/erick/carnavalmanager/data'


firstnames = set()
lastnames = set()
probabilities = []

mestre = 0
for filename in glob.glob(os.path.join(path, '*.txt')):
    onename = 0
    twonames = 0

    f = open(filename, 'r')
    category = filename.split('/')[-1][:-4]

    lines = f.readlines()

    for line in lines:
        names = line.split(" ", 1)
        if len(names) > 1:
            firstnames.add(names[0].strip("\n"))
            lastnames.add(names[1].strip("\n"))
            twonames = twonames + 1
            if names[0].strip("\n").startswith("Mestr"):
                mestre = mestre + 1
        else:
            firstnames.add(names[0].strip("\n"))
            onename = onename + 1

    filename1 = path + "/names/" + category + "first.txt"
    filename2 = path + "/names/" + category + "last.txt"

    output1 = open(filename1, 'w')
    for item in firstnames:
        output1.write(item + "\n")
    output1.close()

    output2 = open(filename2, 'w')
    for item in lastnames:
        output2.write(item + "\n")
    output2.close()
    prob1 = onename / (onename + twonames)
    prob2 = twonames / (onename + twonames)
    if category == 'bateria':
        probabilities.append([category, str(prob1), str(prob2),
                             str(mestre / (twonames)) + "\n"])
    else:
        probabilities.append([category, str(prob1), str(prob2) + "\n"])
    print (category, onename, twonames)

filename3 = path + "/names/" + "stats.txt"
output3 = open(filename3, 'w')
for item in probabilities:
    output3.write(' '.join(item))
output3.close()
