def is_amicable(a,b):
    fac1=0
    fac2=0
    for i in range(1,a):
        if a%i==0:
            fac1+=i
    for j in range(1,b):
        if b%j==0:
            fac2+=j
    if fac1==b and fac2==a:
        print('It is amicable')
    else:
        print("It is non amicable")
is_amicable(220,284)

def fact(a):
    facts=0
    for i in range(1,a):
        if a%i==0:
            print(i)
fact(126)
fact(245)
fact(754)

def is_armstrong(a):
    pow=len(str(a))
    n=a
    res=0
    while n>0:
        digit=n%10
        res+=digit**pow
        n//=10
    if res==a:
        print('It is armstrong number')
is_armstrong(153)

def is_prime(a):
    fact=0
    for i in range(1,a+1):
        if a%i==0:
            fact+=1
    if fact==2:
        print("It is a prime")
    else:
        print("It is a non prime")

is_prime(5)

def gcd(a,b):
    if (a==0 or b==0):
        return 0
    if (a==b):
        return a
    if (a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

def coprime(a,b):
    if gcd(a,b)==1:
        print("Co-prime")
    else:
        print("Not Co-Prime")

coprime(5,6)
coprime(8,16)