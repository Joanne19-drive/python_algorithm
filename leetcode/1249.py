# 1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = s.count(")")
        # "("가 등장했을 떄 짝이 안맞으면 바로바로 지우기 위해
        # 미리 ")"의 값을 받아두지 않고 "("가 등장할 떄마다 오른쪽에 있는 ")"를 count하면 시간초과
        result = ''
        for i in range(len(s)):
            if s[i] == "(":  # 오른쪽에 남는 페어가 있으면 right를 하나 지우고 result에 추가 없으면 넘어가기
                if right != 0:
                    right -= 1
                    left += 1  # ")"가 등장할 떄 왼쪽에 자신의 페어이 있다는 걸 알려주기 위한 신호
                else:
                    continue
            if s[i] == ")":  # 왼쪽에 남는 페어가 있으면 추가 없으면 넘어가기
                if left != 0:
                    left -= 1
                else:
                    right -= 1
                    continue
            result += s[i]
        return result
