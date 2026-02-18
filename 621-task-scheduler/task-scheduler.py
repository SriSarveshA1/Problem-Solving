import heapq

class Solution:

    def heap_push(self,pq,priority,char):
        heapq.heappush(pq,(-priority,char))
    
    def heap_pop(self,pq):
        priority,char = heapq.heappop(pq)
        return -priority,char

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Try to create freq map of tasks
        freq_map = dict()
        pq = []

        for task in tasks:
            if task in freq_map:
                freq_map[task] += 1
            else:
                freq_map[task] = 1
        
        for char,priority in freq_map.items():
            self.heap_push(pq,priority,char)
        
        print("pq=",pq)

        res = []
        while( len(pq)!=0 ):
            poped_elems = []
            for i in range(0,n+1):
                if (len(pq)==0):
                    break
                freq,char = self.heap_pop(pq)
                poped_elems.append(char)
                res.append(char)
            
            #print("res = ",res)
            # We iterate the poped_elems ,reduce its freq by 1 and see whether it can be inserted again to heap
            for poped_elm in poped_elems:
                freq_of_poped_elem = freq_map[poped_elm]
                freq_of_poped_elem-=1
                freq_map[poped_elm] = freq_of_poped_elem
                if freq_of_poped_elem > 0:
                    self.heap_push(pq,freq_of_poped_elem,poped_elm)
            
            if len(poped_elems) < n+1 and len(pq)>0:
                diff_len_popped_elms_and_n_plus_1 = n+1 - len(poped_elems)
                for i in range(diff_len_popped_elms_and_n_plus_1):
                    res.append("idle")
            
            
            
        return len(res)







        
        

        

        