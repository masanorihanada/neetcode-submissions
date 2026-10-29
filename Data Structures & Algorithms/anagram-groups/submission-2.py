from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 💡 キーがなければ自動で空のリスト [] を作ってくれる魔法の辞書
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. アルファベット26文字分の「文字カウント用の箱」を0で初期化
            count = [0] * 26
            
            # 2. 単語の文字を1文字ずつ数える (aはインデックス0、bは1、cは2...)
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # 3. 💡超重要：リスト [0,1,0...] を、辞書のキーにできる「タプル」に変換
            #    同じ文字の出現頻度を持つ単語は、すべて同じキーのバケットに集まります
            anagram_map[tuple(count)].append(word)
            
        # 4. 最後に、きれいにグループ分けされた「値（リストのリスト）」だけを返す
        return list(anagram_map.values())