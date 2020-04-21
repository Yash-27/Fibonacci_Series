list1=[12,-7,5,64,-14]

for i in range(5):
    if list1[i]>0:
        print(list1[i])

list2=[12, 14, -95, 3]

list3=[0,0,0]

j=0
for i in range(4):
    if list2[i]>0:
        list3[j]=list2[i]
        j+=1

list3=[list3[0], list3[1], list3[2]]

print(list3)

print("\U0001F60F")