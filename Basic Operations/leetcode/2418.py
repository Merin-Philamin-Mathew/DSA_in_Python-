from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = zip(names, heights)
        l = sorted(l, key=lambda x: x[1], reverse=True)
        return [i[0] for i in l]   
    
solution = Solution()
result = solution.sortPeople(["qqq","www","ttt","uuu"],[8,405,3,2])
print("result",result)
