
set = [2 ,3 ,4 ,6 ,8 ,4 ,5 ,8 ];


print("Elements present on even position up to fourth index.")

for i in range(1,4,2):
    print (set[i])


print ("Original")

for i in range(0,len(set)):
    print (set[i])

print ("Reverse")

for i in range(len(set)-1,-1,-1):
    print (set[i])

