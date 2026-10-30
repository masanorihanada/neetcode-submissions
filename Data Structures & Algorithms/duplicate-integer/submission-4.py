class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen_hash = set()
        for n in nums:
            if n in already_seen_hash:
                return True
            else:
                already_seen_hash.add(n)

        return False