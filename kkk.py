numberOfShoes=int(input())
sizeOfShoe=[]
c=input().split()
for j in c:
    sizeOfShoe.append(int(j))
print(sizeOfShoe)
numberOfCustomer=int(input())
sizeWithPrice=[]

for i in range(numberOfCustomer):
    list=[]
    c=input().split()
    for j in c:
        list.append(int(j))
    sizeWithPrice.append(list)


total=[]
for i in sizeWithPrice:
    if i[0] in sizeOfShoe:
        total.append(i[1])
        sizeOfShoe.remove(i[0])

print(sum(total))
