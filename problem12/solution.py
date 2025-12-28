from enum import Enum

class RomanVal(Enum):
    I = [1, "I"]
    V = [5, "V"]
    X = [10, "X"]
    L = [50, "L"]
    C = [100, "C"]
    D = [500, "D"]
    M = [1000, "M"]

class Solution:
    def intToRoman(self, num: int) -> str:
        # val : str = ""

        num_list = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman_list = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        
        index : int = 0

        while (num > 0):
            # print(f"index is {index} and num is {num}")
            if (num >= num_list[index]):
                val += roman_list[index]
                num -= num_list[index]
            else:
                index += 1

        return val
        cs = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        vs = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        ans = []
        for c, v in zip(cs, vs):
            while num >= v:
                num -= v
                ans.append(c)
        return ''.join(ans)
            

def main():
    input : int = 3749
    output = Solution().intToRoman(input)
    print(f"output is {output}")

if __name__ == '__main__':
    main()