from enum import Enum

class PatternType(Enum):
    NONE = 0
    STAR = 1
    DOT = 2
    BOTH = 3

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern_type = PatternType.NONE
        for i in range(len(p)):
            # print(p[i])
            if p[i] == "*":
                if pattern_type == PatternType.DOT:
                    pattern_type = PatternType.BOTH
                else:
                    pattern_type = PatternType.STAR
            elif p[i] == ".":
                if pattern_type == PatternType.STAR:
                    pattern_type = PatternType.BOTH
                else:
                    pattern_type = PatternType.DOT

        if pattern_type == PatternType.NONE:
            if s == p:
                return True
            else:
                return False
        elif pattern_type == PatternType.STAR:
            return True
        elif pattern_type == PatternType.DOT:
            return True
        elif pattern_type == PatternType.BOTH:
            return False

def main():
    s = "aa"
    p = "a"
    result = Solution().isMatch(s, p)
    print(result)

if __name__ == "__main__":
    main()