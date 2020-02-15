def comb(str1,str2):
	for ele in str1:
		for ele1 in str2:
			

# def checkmax(arr,k):
# 	i=0
# 	x=[]
# 	sum=0
# 	for j in range(len(arr)):
# 		if arr[i]>k:
# 			x.append(j)
# 			i+=1
# 	if i>=2:
		
# 		first=min(arr)
# 		arr.remove(first)
# 		while first>k:
# 			first-=1
# 		sum+=first
# 		print(first)

# 		second=max(arr)
# 		arr.remove(second)
# 		while second>1:
# 			second-=1
# 		sum+=1
# 		print(second)
	
# 	for ele in arr:
# 		print(arr)
# 		sum+=ele

# 	return sum

# test=int(input())
# for i in range(test):
# 	arr1=list(int(i) for i in input().strip().split(" "))
# 	arr=list(int(i) for i in input().strip().split(" "))
arr=[2,3,2]
k=1
print(checkmax(arr,k))
	#print(checkmax(arr,arr[1]))
