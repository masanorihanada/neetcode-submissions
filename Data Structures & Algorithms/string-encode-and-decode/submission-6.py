class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = "" #empty string
        for s in strs:
          encoded_str += str(len(s)) + "X" + s # length of s + "X" (separator for decoding) + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = [] # list of output (decoded strings)
        i = 0 # location index 
        while i < len(s):
            # Find X first, to know the length of a word 
            j = i
            while s[j] != "X":
                j += 1
            length = int(s[i:j]) # read the length as str and convert it to integer
            start_index = j+1 # location index at the beginning of the word
            end_index = start_index + length # location index at the end of the word
            decoded_str.append(s[start_index:end_index])
            i = end_index # Go to the next word
        return decoded_str