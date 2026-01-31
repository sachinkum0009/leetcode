"""
744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
"""

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        # remove duplicates
        letters = list(dict.fromkeys(letters))
        # sort the letters
        letters.sort()
        for letter in letters:
            if ord(target) < ord(letter):
                res = letter
                break

        return res


def main():
    letters = ["x","x","y","y"]
    target = "z"
    res = Solution().nextGreatestLetter(letters, target)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
