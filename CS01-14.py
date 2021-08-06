list = [5,10,15,20,25,20]

for i in range(len(list)):
    print (i)
    if (list[i] == 20):
         list[i] = 200
print(list)