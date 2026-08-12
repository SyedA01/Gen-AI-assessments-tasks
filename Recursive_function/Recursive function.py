#Recursive function : If a function that calls itself repeatedly inside a single call is known as Recursive function

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print('The factorial of 5 is ',factorial(5))

def climbingways(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return climbingways(n-1) + climbingways(n-2)

print("The number of ways to reach step 4 is :",climbingways(4))


def find_parking_slot(slots,index=0):
    if index>=len(slots):
        return -1
    if slots[index]==0:
        return index
    return find_parking_slot(slots,index+1)

slots=[1,1,1,1,1,0,1,1,1]
result=find_parking_slot(slots)+1
print(f'slot number is {result}')