class Solution(object):
  


    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        queue = []
        for i in range(0,len(tickets)):
            queue.append((i,tickets[i]))

        print(queue)
        while(len(queue)!= 0):
            count = count+1
            pair = queue.pop(0)
            print("........",pair)
            index_pair = pair[0]
            index_value = pair[1]
        
            index_value = index_value - 1

            if(index_value>0):
                queue.append((index_pair,index_value))
            else:
                if(index_pair == k):
                    break

        
        return count
