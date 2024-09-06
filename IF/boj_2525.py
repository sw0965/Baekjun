import sys

# input = sys.stdin.readline

hour, min = map(int, input().split())
cooktime = int(input())
cookhour, cookmin = cooktime//60, cooktime%60


hour += cookhour
min += cookmin

if min >= 60:
    
    hour += min//60
    min = min%60

if hour >= 24:
    hour = hour%24


print("{} {}".format(hour, min))

"""
2중 if 문으로 min if 문 안에 hour if 문도 써서 위 cookhour 값이 24가 되었음에도 min 값이 60 이하면 실행되지 않았음.. 초보적인 실수..;;;;
"""