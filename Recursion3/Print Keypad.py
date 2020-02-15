# Print Keypad
# Send Feedback
# Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important. Just print different strings in new lines.
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

def printkeypad(n,outputsofar):
    if n==0:
        print(outputsofar)
        return
    smallnumber=n//10
    lastdigit=n%10
    
    optionsforlastdigit=getstring(lastdigit)
    for c in optionsforlastdigit:
        newoutput=c+outputsofar
        printkeypad(smallnumber,newoutput)
        
def getstring(alpha):
    if alpha==2:
        return "abc"
    if alpha==3:
        return "def"
    if alpha==4:
        return "ghi"
    if alpha==5:
        return "jkl"
    if alpha==6:
        return "mno"
    if alpha==7:
        return "pqrs"
    if alpha==8:
        return "tuv"
    if alpha==9:
        return "wxyz"
    return " "
#main
x=int(input())
printkeypad(x,"")