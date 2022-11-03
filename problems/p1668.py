class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        times = 0
        while word*times in sequence:
            w = word*times
            i = sequence.index(w)
            # print(f"{' '*i}{w}")
            # print(sequence)
            times+=1
        return times-1
            
    
if __name__ == '__main__':
    i = Solution().maxRepeating(
        "aaabaaaabaaabaaaabaaaabaaaabaaaaba",
        "aaaba"
    )
    print(i)