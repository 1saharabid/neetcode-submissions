class Solution:

    # combine array values in strs to form a string
    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += word
            output += "~" #to concatinate use +=

        return output
        

    # insert each word/char in str (seperated by space) into array
    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        
        i = 0
        while i < len(s):
            if s[i] != "~": 
                    word += s[i]
            else:
                strs.append(word)
                word = ""
            i += 1
        return strs
