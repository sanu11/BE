count=16 
A=[]
P=[]
S=[]
num1=0
num2=0
def complement(num_bin,counter):
    num_complement = num_bin
    i=0
    # ones complement
    while i<=counter:
        if num_bin[i] == 0:
            num_complement[i]=1
        else:
            num_complement[i]=0
        i+=1

    # add 1
    i=counter
    while i>=0:
        if num_complement[i]==1:
            num_complement[i]=0
        else:
            num_complement[i]=1
            break
        i-=1

    return num_complement

def binary_to_decimal(P):
    sum=0
    flag=0
    if(P[0]==1):
        complement(P,15)
        flag=1
        print P
    for i in range(count):
        sum+=P[i]*pow(2,15-i)
    if flag:
        sum = sum*-1
    return sum

def decimal_to_binary(num):
    i=7
    flag=0
    if num < 0:
        flag=1
        num = -1*num
    num_bin=[0 for x in range(8)]
    while i>=0 and num!=0:
        num_bin[i] = num%2
        num/=2
        i-=1
    if(flag):
        # print num_bin
        return complement(num_bin,7)
    return num_bin

def add(P,L):
    c=0
    i=count
    while i>=0:
        temp = P[i] + L[i] + c
        c = temp/2
        P[i] = temp%2
        i-=1

def rightshift(P):
    i=count
    while i>0:
        P[i]=P[i-1]
        i-=1
    return P

def multiply(num1,num2):
    print "Entered Numbers : ", num1, " " ,num2
    num1_bin = decimal_to_binary(num1)
    temp = list(num1_bin)
    print "Binary for  " , num1, " : " , temp
    num2_bin = decimal_to_binary(num2)
    num1_complement = complement(temp,7)

    print "Binary for  " , num2, " : " ,num2_bin
    print "Complement for " , num1 , " : " , num1_complement

    A = [0 for x in range(count)]
    S = [0 for x in range(count)]
    P = [0 for x in range(count)]

    A.append(0)

    S.append(0)
    for i in range(8):
        A[i] = num1_bin[i]
        S[i] = num1_complement[i]
        P[8+i] = num2_bin[i]

    P.append(0)
    print "A : ", A
    print "S : ", S
    print "P : ", P


    for i in range(8):
        if P[-1] == 0 and P[-2] == 0 or P[-1] == 1 and P[-2] == 1:
            rightshift(P)
            print "Right Shift : " , P
        elif P[-2] == 0 and P[-1] == 1:
            add(P,A)
            print "Add P and A : " , P
            rightshift(P)
            print "Right Shift : " , P
        elif P[-2] == 1 and P[-1] == 0:
            add(P,S)
            print "Add P and S : ",  P
            rightshift(P)
            print "Right Shift : " , P

    res = binary_to_decimal(P)
    print res
    return res