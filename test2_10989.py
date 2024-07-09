#계수정렬
import sys
n = int(sys.stdin.readline())
cnt = [0]*10001

for i in range(n):
    numbers = int(sys.stdin.readline())

    cnt[numbers]  += 1

for i in range(10001):
    if cnt[i] !=0:
        for _ in range(cnt[i]):
            print(i)
import psutil
def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")
memory_usage('#1')