class Solution(object):
    def merge(self,arr, l, mid, r): 
        # code here
        
        size1 = mid+1
        size2 = (( r -(mid+1)) +1 )
        merge_size = size1+size2
        temp = []
        
        i = l
        j = mid+1
        
        while(i<=mid and j<=r):
            
            if arr[i]>=arr[j]:
                
                temp.append(arr[j])
                j=j+1
                
            else:
                temp.append(arr[i])
                i = i+1
                
        
        while(i<=mid):
            temp.append(arr[i])
            i = i+1
            
        
        while(j<=r):
            temp.append(arr[j])
            j=j+1
            
            
        
        i = 0
        
        
        for index in range(l,r+1):
            arr[index] = temp[i]
            i=i+1
        
            
        
        
        
    def mergeSort(self,arr, l, r):
        #code here
        
        if l>=r:
            return 
        
        mid = (l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)

    
    def sortArray(self, num):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = num
        l=0
        r=len(arr)-1
        self.mergeSort(arr,l,r)
        for i in range(0,len(num)):
            num[i]=arr[i]
        return num
