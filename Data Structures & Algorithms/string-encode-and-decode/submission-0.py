class Solution:

    def encode(self, strs: List[str]) -> str:
        new_word = ""
        for word in strs:
            new_word += '#' + str(len(word)) + '#' + word
        return new_word

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            j = i+1
            while s[j] != '#':
                j += 1 
            length = int(s[i+1:j])
            word = s[j+1:j+length+1]
            lst.append(word)
            i = j + length + 1

        return lst