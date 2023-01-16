class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        split1 = sentence1.split(' ')
        split2 = sentence2.split(' ')
        while split1 and split2:
            if split1[0] == split2[0]:
                split1.pop(0)
                split2.pop(0)
            elif split1[-1] == split2[-1]:
                split1.pop()
                split2.pop()
            else:
                return False
        return not split1 or not split2