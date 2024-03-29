class Solution(object):
    def calculate_the_nth_day(self, year, month, date, no_days_for_m, is_leap_year):
        
        no_of_days = 0

        i = 1 # starts in january

        while(i<month):
            if i == 2 and is_leap_year:
                no_of_days +=no_days_for_m[i] + 1
            else:
                no_of_days +=no_days_for_m[i]
            i+=1

        
        no_of_days += date
        
        return no_of_days

    def dayOfYear(self, date):
        """
        :type date: str
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
        
        year = int(date[:4])
        month = int(date[5:7])
        date = int(date[8:])

        is_leap_year = False

        if year%100 == 0:
            if year%400 == 0:
                is_leap_year = True
        else:
            if year%4 == 0:
                is_leap_year = True
       

        print("year = ",year)
        print("month = ",month)
        print("date = ",date) 
        print("is_leap_year = ",is_leap_year)

        return self.calculate_the_nth_day(year,month,date,no_days_for_m, is_leap_year)

