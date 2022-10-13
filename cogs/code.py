marks = [['Andrew', 51], ['John', 742], ['Aliya', 95]]

#sort by alphabetical order

def sortalphabet(nstlist):
    secondlist = []
    for i in range(len(marks)):
        secondlist.append(nstlist[i][0])

    return secondlist

ok = sorted(sortalphabet(marks))

#sort by marks

def sortmarks(nstlist):
    secondlist = []
    for i in range(len(marks)):
        secondlist.append(nstlist[i][1])

    return secondlist

oki = sorted(sortmarks(marks))



print(marks)
print("Ordered in alphabetical order: ", ok)
print("Ordered in numerical order: ", oki)