
# def test(a,b):
#     sum=0
#     if a == 0:
#         sum+=b
        
#         return sum
    
#     for i in range(1,b+1):

#         sum+=test(a-1,i)

#     return sum

# for i in range(0, int(input())):
#     a,b=[int(input()) for _ in range(0,2)]
#     print(test(a,b))


for i in range(0, int(input())):
    a,b=[int(input()) for _ in range(0,2)]
    L2=[[0]*15 for _ in range(0,a+1)]

    for i in range(1,15):
        L2[0][i]=i
    for i in range(1,a+1):
        for j in range (1,15):
            L2[i][j]= L2[i][j-1]+L2[i-1][j]

# print(L2)
    print(L2[a][b])

    