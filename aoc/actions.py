from .bureaucrat import Stenographer
from .fetch import BudgetFetch
from .parsers import DataParser, MainParser


class Question:
    @staticmethod
    def view(year, day):
        query = BudgetFetch()
        parser = MainParser()

        html = query.get_question(year, day)
        parser.feed(html)

        parser.print_text


class Data:
    @staticmethod
    def view(year, day):
        query = BudgetFetch()
        parser = DataParser()
        recorder = Stenographer()

        html = query.get_input(year, day)
        recorder.record(html, year, day)
        parser.feed(html)

        parser.print_text


class Submit:
    @staticmethod
    def view(year, day, answer, part):
        query = BudgetFetch()
        parser = MainParser()

        html = query.post_answer(year, day, answer, part)
        parser.feed(html)

        parser.print_text


class Action:
    def __init__(self, day, command, answer=None, part=None):
        self.day = day
        self.year = 2022
        self.command = command
        self.answer = answer
        self.part = part

    def do(self):
        match self.command:
            case "question":
                Question.view(self.year, self.day)
            case "data":
                Data.view(self.year, self.day)
            case "submit":
                if None in (self.answer, self.part):
                    raise ValueError(
                        f"Neither answer nor part cannot be None, you provided: {self.answer!r}, {self.part!r}"
                    )
                Submit.view(self.year, self.day, self.answer, self.part)
            case _:
                raise ValueError(f"Unrecognized command: {self.command!r}")
