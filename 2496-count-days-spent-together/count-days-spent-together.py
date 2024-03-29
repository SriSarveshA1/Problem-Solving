class Solution(object):


    def calculate_the_nth_day(self,month,date,no_days_for_m):
        
        no_of_days = 0

        i = 1 # starts in january

        while(i<month):
            no_of_days +=no_days_for_m[i]
            i+=1

        
        no_of_days += date
        
        return no_of_days


    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        no_days_for_m = dict()
      
        no_days_for_m[1]=31
        no_days_for_m[2]=28
        no_days_for_m[3]=31
        no_days_for_m[4]=30
        no_days_for_m[5]=31
        no_days_for_m[6]=30
        no_days_for_m[7]=31
        no_days_for_m[8]=31
        no_days_for_m[9]=30
        no_days_for_m[10]=31
        no_days_for_m[11]=30
        no_days_for_m[12]=31

        arriveAlice = self.calculate_the_nth_day(int(arriveAlice[:2]), int(arriveAlice[3:]), no_days_for_m)
        leaveAlice = self.calculate_the_nth_day(int(leaveAlice[:2]), int(leaveAlice[3:]), no_days_for_m)

        arriveBob = self.calculate_the_nth_day(int(arriveBob[:2]),int(arriveBob[3:]),no_days_for_m)
        leaveBob = self.calculate_the_nth_day(int(leaveBob[:2]),int(leaveBob[3:]),no_days_for_m)

        print("arriveAlice = ",arriveAlice)
        print("leaveAlice = ",leaveAlice)
        print("arriveBob = ",arriveBob)
        print("leaveBob = ",leaveBob)

        if (arriveAlice<=arriveBob and arriveBob<=leaveAlice):
            
            if leaveBob<=leaveAlice:
                return (leaveBob - arriveBob)+1

            else:
                return (leaveAlice - arriveBob)+1
        
        if (arriveBob<=arriveAlice and arriveAlice<= leaveBob):
            
            if leaveAlice<=leaveBob:
                return (leaveAlice - arriveAlice)+1
            else:
                return (leaveBob - arriveAlice)+1

        return 0

      
          