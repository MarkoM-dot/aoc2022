from abc import ABC, abstractmethod
from html.parser import HTMLParser


class Parser(ABC):
    @abstractmethod
    def feed(self):
        ...

    @abstractmethod
    def print_text(self):
        ...


class MainParser(HTMLParser, Parser):
    text = []

    def extract_main(self, data) -> str:
        """
        Extract only the dominant content in the html and strip the excess details.
        """
        start = data.find("<main>") + len("</main>")
        end = data.find("</main>")
        return data[start:end]

    def feed(self, data):
        r"""
        This method has been customized for AOC.

        Feed data to the parser.

        Call this as often as you want, with as little or as much text
        as you want (may include '\n').
        """
        self.rawdata = self.rawdata + self.extract_main(data)
        self.goahead(0)

    def handle_endtag(self, tag) -> None:
        match tag:
            case "h2":
                self.text.append("\n")
                self.text.append("\n")
            case "p":
                self.text.append("\n")
            case _:
                pass

    def handle_data(self, data):
        self.text.append(data)

    @property
    def print_text(self):
        print("".join(self.text))


class DataParser(Parser):
    text = []

    def feed(self, data):
        self.text.append(data)

    @property
    def print_text(self):
        print("".join(self.text))
