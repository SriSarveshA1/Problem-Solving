class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        braq_map = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for ele in s:
            if ele not in braq_map:
                stack.append(ele)
            else:
                if len(stack)!=0 and stack[len(stack)-1] == braq_map[ele]:
                    stack.pop(len(stack)-1)
                else:
                    return False
        
        if len(stack)!=0:
            return False

        return True




        