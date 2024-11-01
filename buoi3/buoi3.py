# import math
# def Max_arr(arr, l, r):
#     if l == r:
#         return arr[l]
#     m = (l + r) // 2
#     return max(Max_arr(arr, l, m), Max_arr(arr, m + 1, r))


# n = int(input()) 
# arr = []
# for i in range(n):
#     x = int(input())
#     arr.append(x)
# res = Max_arr(arr,0,n-1)
# print(res)

# arr = [ 1 , 2 , 'a' , 'b', "gg" , [1 , 1 , 1 , (1 , 1)]]
# for index in range(len(arr)):
#     print(index , arr[index])
    
# print()
# for index , i in enumerate(arr):
#     print(f'index={index} , values:{i}')

# dem = 0
# while 1 :
#     print('Thanh')
#     dem += 1
#     if(dem == 5 ):
#         break 

# a = [ 1 , 2 , 3 , 4 , 5]
# b = [6 , 6 , 6 , 6 ]
# arr = list(zip(a,b))

# for index , (i,j)  in enumerate(arr):
#     print(index , i,j)

const = 50

def gt(n):
    if n == 1 :
        return 1
    return n * gt(n-1)

s = input()
if s == 'sin':
    x =float(input())
    for n in range(1,const):
        # y = (-1)**n * (x**(2*n+1))/gt(2*n+1) 
        # print(y)
        x += ((-1)**n) * (x**(2*n+1))/gt(2*n+1)
    print(x)
elif s == 'cos':
    x = float(input())
    for n in range(1,const):
        x += ((-1)**n) * (x**(2*n))/gt(2*n)
    print(x)
else:
    print("Em nhap sai roi cu")