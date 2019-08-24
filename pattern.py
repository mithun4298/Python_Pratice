# for i in range(10):
#     for j in range(i+1):
#         print('*',end='')
#     print("")
#...........................................................
# for i in range(1,11):
#     print('*'*i,end='\n')
# print()
#...........................................................

n=10
for i in range(1,11):
    print(' '*n,end='')     #equilateral print
    print(('*'*i)*2,end='')
    print(' ' * n*2, end='')
    print(('*' * i) * 2)
    n=n-1
    l=n+1
for i in range(10,0,-1):
    print(' '*l,end='')     #equilateral print
    print(('*'*i)*2,end='')
    print(' ' * l*2, end='')  # equilateral print
    print(('*' * i) * 2)
    l=l+1



#...........................................................
#Printing Floyd’s triangle pattern
# c=1
# for i in range(1,7):
#     for j in range(c,i+c):
#         print(j,end=' ')
#         c=c+1
#     print()

#..............................................................
# n = 10
# for i in range(1,7):
#     num = 1
#     print(' ' * n, end='')
#     for j in range(1, i+1):
#         print(num, end=' ')
#         num = num*(i-j)//j
#     n = n-1
#     print()
#.................................................................