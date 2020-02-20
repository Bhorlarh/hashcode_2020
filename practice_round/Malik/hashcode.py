import string
import random
file = str(input("Enter file name :"))
f = open("../Problems/"+file+".in",  "r")
f1 = f.readlines()
datas = []

for x in f1:
    x = x.split(" ")
    for i in range (0 , len(x)):
        datas.append(x[i])

sizes = []
for i in range(2 , len(datas)):
    sizes.append(int(datas[i]))
sizes = sizes[::-1]



maxsize = int(datas[0])

orderedslice = 0

orderedtypes=[]

types = 0



for i in range (0 , (len(sizes))):
    if (orderedslice + sizes[i]) > maxsize :
        orderedslice +=0
    else:
        orderedslice+=sizes[i]
        orderedtypes.append((len(sizes)-1) - i)
        types+=1

orderedtypes = orderedtypes[::-1]

file2 = open("../Solutions/"+file+"_submission"+".in" , "w")
file2.write(""+str(types)+"\n")
for i in orderedtypes:
    file2.write(str(i) + " ")
print(orderedslice)
print(orderedtypes)
print("we ordered " + str(types))
