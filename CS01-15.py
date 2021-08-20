def my_list(list):
    for i in range(len(list)):
        if (list[i] == 20):
            list[i] = 200
    print(list)

list = [5,10,15,20,25,20]
my_list(list)