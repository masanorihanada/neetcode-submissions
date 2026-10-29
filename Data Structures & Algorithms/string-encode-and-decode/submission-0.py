class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "X" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # スキャンする位置のインデックス
        
        while i < len(s):
            # 1. まず 'X' がどこにあるかを探して、長さを表す数字を切り出す
            j = i
            while s[j] != "X":
                j += 1
            length = int(s[i:j])  # 'X' の手前までが「長さ（数字）」
            
            # 2. 'X' の次の位置から、length分の文字列を切り出す
            start_idx = j + 1
            end_idx = start_idx + length
            res.append(s[start_idx:end_idx])
            
            # 3. 処理が終わったので、インデックスを次の単語の先頭まで一気に進める
            i = end_idx
            
        return res