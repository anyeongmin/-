a=int(input(">"))
b=[]
for i in range(2,a):
    for j in range(2,a):
        if i%j==0:
            if i!=j:
                break
            else:
                print(i)
                b.append(i)
print("총 '%d' 개입니다" % len(b))