# Return Keypad
# Send Feedback
# Given an integer n, using phone keypad find out all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important.
# Input Format :
# Integer n
# Output Format :
# All possible strings in different lines
# Constraints :
# 1 <= n <= 10^6
# Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf

def keypad(n):
    #Implement Your Code Here
    if n==0:
        output=[]
        output.append("")
        return output
    
    smallerdigit=n//10
    lastdigit=n%10
    
    smalldigits=keypad(smallerdigit)
    optionsforlastdigit=getstring(lastdigit)
    
    output=[]
    
    for s in optionsforlastdigit:
        for c in smalldigits:
            option=c+s
            output.append(option)
            
    return output
    
    pass

def getstring(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return " "

n = int(input())
ans = keypad(n)
for s in ans:
    print(str(s))
