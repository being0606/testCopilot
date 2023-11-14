###
# 1. 파이썬으로 직육면체 클래스 구현
# 직육면체를 나타내는 Box 클래스를 파이썬으로 작성하세요. Box 인스턴스(객체)는 부피에 따라 비교가 가능해야 합니다. 파이썬에서는 __lt__ 매직 메소드를 구현하여 인스턴스들의 자연스러운 순서(natural ordering)를 정의할 수 있습니다. 이 순서를 사용해 인스턴스들을 정렬할 때 부피에 따라 정렬되도록 하세요.

# 또한, Box 인스턴스를 표면적에 따라 정렬할 수 있도록 하세요. 이를 위해, 정렬 함수에서 key 인자를 사용하여 정렬 기준을 제공할 수 있습니다.

# 요구 사항:
# Box 클래스를 작성하세요. 클래스는 가로(width), 세로(length), 높이(height) 속성을 무작위로 초기화해야 합니다. 이 속성들은 0.0 이상 10.0 미만의 난수여야 합니다.

# 클래스는 다음 기능을 가져야 합니다:
# 부피(volume)를 계산하는 메소드.
# 표면적(surface_area)을 계산하는 메소드.
# 다른 Box 인스턴스와의 비교를 위한 매직 메소드(__lt__).
# Box 인스턴스 다섯 개를 생성하고, 이들을 부피 순으로 정렬하여 출력하세요.

# 동일한 Box 인스턴스들을 표면적 순으로 정렬하여 출력하세요.
####
import random

def main():
    boxes = [Box() for _ in range(5)]
    print('Boxes sorted by volume:')
    for box in sorted(boxes):
        print(box)
    print('Boxes sorted by surface area:')
    for box in sorted(boxes, key=lambda box: box.surface_area):
        print(box)

class Box:
    