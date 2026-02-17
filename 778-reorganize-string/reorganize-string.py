import heapq

class Solution:

    def heap_push(self,pq,priority,char):
        heapq.heappush(pq,(-priority,char))
    
    def heap_pop(self,pq):
        priority,char = heapq.heappop(pq)
        return -priority,char

    def reorganizeString(self, s: str) -> str:
        # 1. Try to add all the chars of the string 's' into a freq map
        # 2. At any point of time for any character the freq is > (n+1)/2 then the result is ""
        # 3. If not we continue
        # 4. We will have a heap (max heap), based on the character freq.
        # 5. Then we pop the element from the heap and try to insert into res="" 
        # 6. If the res[n-1]!= heap.peek() we insert the heap's top char 
            # we do heap.pop() and then decrese the count and again insert into the heap
        # 7. If the res[n-1]==heap.peek() then we pop that element 
            # and keep it in temp,temp_freq = heap.pop()
        # 8. Then we check again for res[n-1] whether its not eq heap.peek() if yes we pop it and decrease the count and enter it back
            # or if there are no elements in the heap we return ""
        
        freq_map = dict()

        n = len(s)

        pq = []

        for char in s:
            if char in freq_map:
                freq_map[char]+=1
            else:
                freq_map[char]=1
            
            if freq_map[char] > (n+1)//2:
                return ""

        print("freq_map",freq_map)

        for key,value in freq_map.items():
            self.heap_push(pq, value, key)

        print("heap...",pq)

            
        res = ""
        while(len(pq)!=0):
            print("///",res)
            freq,char=self.heap_pop(pq)
            print("freq, ",freq)
            print("char, ",char)

            if len(res)==0 or res[len(res)-1] != char:
                print(f"s[n-1]={s[n-1]}, char={char}")
                res += char
                freq=freq-1
                if freq>0:
                    self.heap_push(pq,freq,char)
                continue
            
            # res[n-1] == char
            if (len(pq) == 0):
                return ""
            
            new_freq,new_char = self.heap_pop(pq)
            new_freq = new_freq-1
            res+=new_char

            if new_freq>0:
                self.heap_push(pq, new_freq, new_char)
            
            if freq>0:
                self.heap_push(pq, freq, char)
        
        return res


            

            
            



        
        
            
