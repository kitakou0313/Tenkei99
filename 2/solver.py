from typing import List


def generateAllKakko(N:int) -> List[str]:
    """
    括弧の数一つ毎に再帰的につくれば良さそう
    """
    pass

if __name__ == "__main__":
    N = int(input())

    reses = generateAllKakko(N)

    for res in reses:
        print(res)