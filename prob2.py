# 팩토리얼 함수
# 양의 정수 N의 팩토리얼은 1부터 N까지의 모든 정수의 곱입니다. 예를 들어, 5! (5의 팩토리얼)은 1 * 2 * 3 * 4 * 5 = 120입니다. 0의 팩토리얼은 1로 정의됩니다.

# 파이썬에서 주어진 정수 N의 팩토리얼을 계산하는 factorial 함수를 작성하세요. 함수는 재귀적(recursive)이거나 반복적(iterative)일 수 있습니다.

# 요구 사항:
# 함수 이름은 factorial이어야 합니다.
# 함수는 하나의 인자를 받아야 하며, 이 인자는 계산할 정수 N입니다.
# 함수는 N의 팩토리얼을 반환해야 합니다.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(0))