class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dial = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
            'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        length = len(digits)
        digit_code = []
        for i in range(length):
            digit_code.append(int(digits[i]))
        ans = []
        for i in digit_code:
            if not ans:
                for j in dial[i-2]:
                    ans.append(j)
            else:
                new_ans = []
                for k in ans:
                    for j in dial[i-2]:
                        new_ans.append(k+j)
                ans = new_ans[:]
        return ans
