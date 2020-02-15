# Print Subsequences
# Send Feedback
# Given a string (lets say of length n), print all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.
# Note : The order of subsequences are not important. Print every subsequence in new line.
# Sample Input:
# abc
# Sample Output:
# "" (the double quotes just signifies an empty string, don't worry about the quotes)
# c 
# b 
# bc 
# a 
# ac 
# ab 
# abc 

def printSubsequences(string,o):
    #Implement Your Code Here
    if len(string)==0:
        print(o)
        return
    
    printSubsequences(string[1:],o)
    
    newoutput=o+string[0]
    printSubsequences(string[1:],newoutput)
    pass

string = input()
printSubsequences(string,"")
