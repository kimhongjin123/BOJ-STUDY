b=[i for i in range(1,9)]
c=[i for i in range(8,0,-1)]
a= list(map(int,(input().split())))

if a == b :
    print("ascending")
elif a == c :
    print("descending")
else :
    print("mixed")

