class BookReader:
    def __init__(self, name) -> None:
        self.name = name

    def read_book(self):
        print(f"{self.name}님은 책을 읽는다.")


bookleader = BookReader("철수")

bookleader.read_book()
