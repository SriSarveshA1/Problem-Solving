class Solution:
	def nextSmallerEle(self, arr):
		# code here
		stack = []
		
		
		n = len(arr)
		res = [-1 for i in range(n)]
		
		for i in range(n-1,-1,-1):
		    
		    while len(stack)!=0 and stack[len(stack)-1]>=arr[i]:
		        stack.pop()
		       
		    if len(stack)==0:
		        res[i] = -1
		    else:
		        res[i] = stack[len(stack)-1]
		       
		    
		    stack.append(arr[i])
		   
		return res