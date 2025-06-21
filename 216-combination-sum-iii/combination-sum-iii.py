class Solution:

    def helper(self,i:int ,k:int, n:int,cur:List[int],arr:List[int],res:List[List[int]]):
        if len(cur)>k:
            return 

        if i>=len(arr):
            if len(cur)==k and sum(cur) == n:
                print("cur = ",cur)
                temp = []
                for ele in cur:
                    temp.append(ele)

                res.append(temp)
            
            return 
        
        cur.append(arr[i])
        self.helper(i+1,k,n,cur,arr,res)
        cur.pop()
            
        self.helper(i+1,k,n,cur,arr,res)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        arr = []
        for ele in range(1,10):
            arr.append(ele)

        self.helper(0,k,n,[],arr,res)
        print("..res=",res)
        return res
        