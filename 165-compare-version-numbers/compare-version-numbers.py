class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        array1 = version1.split(".")
        n1 = len(array1)

        array2 = version2.split(".")
        n2 = len(array2)

        max_length = max(n1,n2)

        answer = 0

        for i in range(0,max_length):

            a1_current_revision = ""
            a2_current_revision = ""

            if i >= n1: 
                a1_current_revision = 0
                a2_current_revision = int(array2[i])
            else:
                if i >= n2:
                    a1_current_revision = int(array1[i])
                    a2_current_revision = 0
                else:
                    a1_current_revision = int(array1[i])
                    a2_current_revision = int(array2[i])


            if a1_current_revision == a2_current_revision:
                continue
            else:
                if a1_current_revision>a2_current_revision:
                    return 1
                else:
                    return -1
        return answer

            
