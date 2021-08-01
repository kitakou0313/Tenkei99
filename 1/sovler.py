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
    
    pass

if __name__ == "__main__":
    N, L = map(int, input().split())
    K = int(input())

    A = map(int, input().split())

    print(calMaxYoukanLength(N, L, L, A))