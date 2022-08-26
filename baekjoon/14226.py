from collections import deque

# 내 풀이
S = int(input())

q = deque()
q.append((1, 0, 0))  # (화면에 있는 이모티콘, 클립보드에 있는 이모티콘 개수, 소요시간)

visited = [-1] * 1001
visited[1] = 0

while q:
    emoji, clipboard, cnt = q.popleft()
    if emoji == S:
        print(cnt)
        break
    if clipboard != 0 and emoji + clipboard <= 1000:
        if visited[emoji+clipboard] == -1:
            visited[emoji+clipboard] = cnt+1
        q.append((emoji+clipboard, clipboard, cnt+1))
    if emoji != clipboard:
        q.append((emoji, emoji, cnt+1))
    # 이 부분에서 visited를 emoji + clipboard에서처럼 밑으로 빼려고 했는데 그러면 시간초과가 뜬다.
    # 근데 왜 이 부분을 빼지 않아도 정답처리가 되는지 이해가 안된다.
    # 이런 요상한 풀이는 다른 사람들에게서 찾을 수 없어서 고민을 해봐야겠다,,
    if emoji > 1 and visited[emoji-1] == -1:
        visited[emoji-1] = cnt+1
        q.append((emoji-1, clipboard, cnt+1))

# 모범 풀이
S = int(input())

dp = dict()
dp[(1, 0)] = 0

q = deque()
q.append((1, 0))

while q:
    emoji, clipboard = q.popleft()
    if emoji == S:
        print(dp[(emoji, clipboard)])
        break
    if emoji + clipboard <= 1000 and (emoji + clipboard, clipboard) not in dp:
        dp[(emoji+clipboard, clipboard)] = dp[(emoji, clipboard)] + 1
        q.append((emoji+clipboard, clipboard))
    if (emoji-1, clipboard) not in dp:
        dp[(emoji-1, clipboard)] = dp[(emoji, clipboard)] + 1
        q.append((emoji-1, clipboard))
    if emoji != clipboard and (emoji, emoji) not in dp:
        dp[(emoji, emoji)] = dp[(emoji, clipboard)] + 1
        q.append((emoji, emoji))
