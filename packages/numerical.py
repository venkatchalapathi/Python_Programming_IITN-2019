def checkPrime(sn):
    flag = 0
    if(sn==2):
        return True
    else:
        for i in range(2,sn):
            if(sn%i==0):
                flag = 1
                break
    if(flag == 1):
        return False
    else:
        return True
   
# fldjflds lsdfjlksdj
def primeFactorsList(num):
    ls=[]
    for i in range(2,num+1):
        if(num%i == 0):
            if(checkPrime(i)):
                ls.append(i)
    # print(ls)
    return len(ls) 

def isSpecialNumber(n,p):
    if(primeFactorsList(n)>=p):
        return True
    else:
        return False 