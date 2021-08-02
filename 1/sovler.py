from typing import List

"""
最大何個の長さM以上の区間を作れるかを考え、1~Lについて検証
"""
def isEnableDevideYoukanWithM(A:List[int],K:int ,M:int)->bool:
    periodLen = 0
    periondCnt = 0
    
    for i in range(len(A)):
        periodLen += A[i]
        if periodLen >= M:
            periodLen = 0
            periondCnt += 1
    
    if periondCnt < K:
        return False
    
    return True

def calMaxYoukanLength(N:int, L:int, K:int, A:List[int]) -> int:
    ng = -1
    ok = L

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if isEnableDevideYoukanWithM(A, K, mid):
            ok = mid
        else:
            ng = mid
    return ok

if __name__ == "__main__":
    N, L = map(int, input().split())
    K = int(input())

    A = list(map(int, input().split()))

    print(calMaxYoukanLength(N, L, K, A))