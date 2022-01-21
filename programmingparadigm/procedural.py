# 함수 호출 중심으로 설계한다면 절차지향 프로그래밍
# 조건문의 사용이 빈번한 것이 특징이다.

class Reader:
    def __init__(self, filetype):
        self.filetype = filetype

    def read(self, filepath):
        print(self.filetype + " 편집기를 이용하여 " + filepath + " 을 불러냈습니다.")


def read_input_file(file_path: str) -> str:
    if file_path.endswith(".txt"):
        reader = get_file_reader(file_type="txt")
        return reader.read(file_path)
    elif file_path.endswith(".csv"):
        reader = get_file_reader(file_type="csv")
        return reader.read(file_path)
    else:
        raise ValueError("파일 확장자는 txt, csv 만 사용 가능합니다.")


def get_file_reader(file_type: str) -> Reader:
    return Reader(file_type)


# 특정 기능을 갖는 함수를 중심으로 순서대로 로직이 실행된다.
# 하지만 기능의 확장에 불리하다.
if __name__ == '__main__':
    read_input_file("input.txt")
