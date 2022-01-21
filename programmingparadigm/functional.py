# 함수형 프로그래밍은 외부 값을 참조하지 않는다.
# side effect 제거 목적
def func(a: int, b: int, c: int) -> int:
    return a + b + c


