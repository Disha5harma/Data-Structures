##LCM

def findlcm(x,n):
    if x<n:
    	i=x
    else:
    	i=n
    while(1):
        if i%x==0 and i%n==0:
            lcm=i
           	return lcm
        i+=1


n=int(input())
x=int(input())
print(findlcm(x,n))

##HCF

def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)

a=int(input())
b=int(input())
if b>a:
    b,a=a,b

print(hcf(a,b))