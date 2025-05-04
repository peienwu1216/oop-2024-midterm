class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = list(zip(names, heights))
        paired.sort(key = lambda x:x[1], reverse = True)
        answer = [name for name,_ in paired]
        return answer
