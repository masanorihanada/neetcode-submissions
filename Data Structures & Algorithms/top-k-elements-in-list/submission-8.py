class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # 1. count.items() で [(数字, 回数), (数字, 回数)...] のリストを作る
        # 2. sorted() を使い、2つの基準で同時にソートする！
        sorted_items = sorted(
            count.items(), 
            key=lambda x: (-x[1], x[0])  # 💡 ここが魔法の2段階指定！
        )
        
        # 3. 上位 k 個の「数字（0番目の要素）」だけを切り取って返す
        return [item[0] for item in sorted_items[:k]]

