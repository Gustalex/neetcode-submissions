class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnums = set()
        for i in nums:
            if i in hashnums:
                return True
            hashnums.add(i)
        return False
        