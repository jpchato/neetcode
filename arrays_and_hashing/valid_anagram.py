class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        reversed_t = t[::-1]
        print(s, reversed_t)
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().isAnagram( "anagram", "nagaram"))
    print(Solution().isAnagram( "rat", "car"))