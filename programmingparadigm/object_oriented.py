# 객체지향은 각 클래스가 각자의 역할을 수행한다.
# 프로그램이 객체간 메서드 호출로 이뤄지는 것이다.
# 확장에 굉장히 열려있다. 이를테면 파일 확장자에 jpg, docs 등이 추가되어야 한다고 가정했을때
# 절차지향은 if 문이 계속해서 추가되지만, 객체지향은 아니다.
class FileReader:
    def __init__(self) -> None:
        self.file_types = ["txt", "csv", "xlsx"]
        self.file_history = []

    def read(self, file_path: str) -> str:
        self._validate(file_path)
        print("불러오기 완료")

    # 메서드 앞에 _는 접근제한자 표시
    def _validate(self, file_path: str) -> None:
        for file_type in self.file_types:
            if file_path.endswith(file_type):
                return
        raise ValueError("파일 확장자는 txt, csv, xlsx 중 하냐여야 합니다.")


class DataParser:
    def parse(self, data: str):
        print("data parse completed")
        return self


class Repository:
    def __init__(self):
        self.store = []

    def save(self, parsed_data):
        self.store.append(parsed_data)
        print("save completed")


class Processor:
    def __init__(self,
                 file_reader: FileReader,
                 data_parser: DataParser,
                 repository: Repository) -> None:
        self.file_reader = file_reader
        self.data_parser = data_parser
        self.repository = repository

    def execute(self, file_path: str) -> None:
        data = self.file_reader.read(file_path)
        parsed_data = self.data_parser.parse(data)
        self.repository.save(parsed_data)


if __name__ == '__main__':
    processor = Processor(FileReader(), DataParser(), Repository())
    processor.execute("input.txt")

    try:
        processor.execute("error")
    except ValueError as e:
        print(e)
