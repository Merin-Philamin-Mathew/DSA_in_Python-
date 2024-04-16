from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the least significant digit
        print("1",digits)
        for i in range(n - 1, -1, -1):
            print(i,"ddddddddddddddddd")
            if digits[i] < 9:
                # If the current digit is less than 9, just increment it and return
                print("2",digits)
                print("2",digits[i])
                digits[i] += 1
                print("3",digits)
                print("3",digits[i])
                return digits
            else:
                # If the current digit is 9, set it to 0 and continue to the next digit
                print("4",digits)
                print("4",digits[i])
                digits[i] = 0
    
        # If we reach here, it means all digits were 9 (e.g., [9, 9, 9])
        # In this case, we need to add an additional digit at the front
        print("5",digits)
        return [1] + digits
    
solution = Solution()
result = solution.plusOne([1,4,2,9,9])
print("result",result)