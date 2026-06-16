class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", '')
        a = re.sub(r'[^A-Za-z0-9 \s]', '', s)

        start = 0
        end = len(a) - 1

        while(start < end):
            if (a[start] != a[end]):
                return False
            start +=1
            end -=1
        return True
