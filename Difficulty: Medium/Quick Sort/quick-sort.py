class Solution:
    def partition(self, arr, low, high):
        #code here
        pivot = arr[high]
        i = low
        j = high
        
        while (i<j):
            
            while(i<=high-1 and arr[i]<pivot):
                i+=1
                
            while(j>=low+1 and arr[j]>=pivot ):
                j-=1
        
            if (i<j):
                [arr[i],arr[j]] = [arr[j],arr[i]]
            else:
                break
        
        
        [arr[high],arr[i]] = [arr[i],arr[high]]
        
        return i
        
    def quickSort(self, arr, low, high):
        #code here 
        if (low <= high):
            part_idx = self.partition(arr,low,high)
            self.quickSort(arr,low,part_idx-1)
            self.quickSort(arr,part_idx+1,high)
            
    
        