class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 各要素の出現回数を O(N) で数え上げる
        count = Counter(nums)
        
        # 2. Counterの秘密兵器 .most_common(k) を使う
     
        return [item[0] for item in count.most_common(k)]
