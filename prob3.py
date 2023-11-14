# 주어진 정수의 비트 표현에서 1의 개수를 세어 반환하는 메소드를 작성하세요.
# bitCount라는 이름의 메소드를 작성합니다. 이 메소드는 int 타입 파라미터 하나를 가지며 주어진 int 값이 메모리 내에서 몇 개의 1 비트를 갖는지 세어 그 값을 int 타입으로 반환합니다.

# <JAVA 기반 힌트>
# 왼쪽 끝의 한 비트만 1인  mask를 만든다.
#         int mask = 1 << 31;
# 주어진 정수 input과 mask를 & 연산하면 그 결과는, input의 왼쪽 끝 비트가 0인 경우 0이고, 1인 경우 0이 아니다. 연산 결과가 0이 아니면 count를 증가시킨다.
# mask를 오른쪽으로 한 칸 unsigned시프트시킨다. (왼쪽 끝에 0이 들어간다.)     
#         mask = mask >>> 1
# 주어진 정수 input과 mask를 & 연산하면 그 결과는, input의 왼쪽 끝 두 번째 비트가 0인 경우 0이고, 1인 경우 0이 아니다. 연산 결과가 0이 아니면 count를 증가시킨다.
# 위 과정을 반복한다. mask의 비트들이 모두 0이 될 때까지.
# 마지막으로 count를 반환한다.

def main():
    input_number = int(input("32 bit integer: "))
    count = bin(input_number).count('1')
    print(f"{input_number} has {count} number of '1's")

if __name__ == "__main__":
    main()


