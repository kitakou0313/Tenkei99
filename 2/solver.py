from typing import List, Set

def isValid(string:str) -> bool:
    """
    正しい括弧文字列か判定
    """
    leftKakkoNum = 0
    rightKakkoNum = 0

    for char in string:
        if char == "(":
            leftKakkoNum += 1
        else:
            rightKakkoNum += 1
        if rightKakkoNum > leftKakkoNum:
            return False

    if not(leftKakkoNum == rightKakkoNum):
        return False
    
    return True

def generateAllKakko(N:int) -> List[str]:
    """
    括弧の数一つ毎に再帰的につくれば良さそう -> ダメ
    bit全探索でやる
    """
    # 奇数長の長さは生成できないので
    if N % 2 == 1:
        return []
    
    resSet:List[str] = []
    for bit in range(0, 2**N):
        trgString = "".join(["(" if (bit >> ind) & 1 else ")" for ind in range(0, N)])
        if isValid(trgString):
            resSet.append(trgString)

    return resSet

if __name__ == "__main__":
    N = int(input())
    reses = generateAllKakko(N)

    sortedRes = sorted(reses)

    for res in sortedRes:
        print(res)