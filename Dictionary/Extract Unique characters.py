# Extract Unique characters
# Send Feedback
# Given a string, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same.
# Input format :
# String S
# Output format :
# Output String
# Constraints :
# 1 <= Length of S <= 50000
# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd
# Sample Input 2 :
# abcde
# Sample Output 2 :
# abcde


def uniqueChars(string):
    # Please add your code here
    dict={}
    ans=[]
    for s in string:
        if s in dict:
            dict[s]+=1
        else:
            dict[s]=1
            print(s,end="")

    pass

# Main
string = input()
uniqueChars(string)