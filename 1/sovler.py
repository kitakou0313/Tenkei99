from typing import List

"""
最大何個の長さM以上の区間を作れるかを考え、1~Lについて検証
"""
def isEnableDevideYoukanWithM(A:List[int],K:int ,M:int)->bool:
    pre = 0
    periondCnt = 0
    
    for i in range(0, len(A)):
        if ((A[i] - pre >= M) and (L - A[i] >= M)):
            periondCnt += 1
            pre = A[i]
    
    if periondCnt >= K:
        return True
    
    return False

def calMaxYoukanLength(N:int, L:int, K:int, A:List[int]) -> int:
    ng = -1
    ok = L+1

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if isEnableDevideYoukanWithM(A, K, mid):
            ng = mid
        else:
            ok = mid
            
    return ng

if __name__ == "__main__":
    N, L = map(int, input().split())
    K = int(input())

    A = list(map(int, input().split()))

    print(calMaxYoukanLength(N, L, K, A))