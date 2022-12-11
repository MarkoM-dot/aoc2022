import urllib.parse
import urllib.request


class BudgetFetch:
    """
    Fetch Advent of Code Information.
    """

    def _get_url(self, year: int, day: int) -> str:
        return f"https://adventofcode.com/{year}/day/{day}"

    def _get_cookie(self) -> dict[str, str]:
        with open(".cookie") as f:
            contents = f.read().strip()
        return {"Cookie": contents, "User-Agent": "MarkoM-dot, hello Eric!"}

    def get_question(self, year: int, day: int) -> str:
        req = urllib.request.Request(
            self._get_url(year, day), headers=self._get_cookie()
        )
        return urllib.request.urlopen(req).read().decode()

    def get_input(self, year: int, day: int) -> str:
        url = self._get_url(year, day) + "/input"
        req = urllib.request.Request(url, headers=self._get_cookie())
        return urllib.request.urlopen(req).read().decode()

    def post_answer(self, year: int, day: int, answer: str, part: int) -> str:
        url = self._get_url(year, day) + "/answer"
        params = urllib.parse.urlencode({"level": part, "answer": answer})

        req = urllib.request.Request(
            url,
            method="POST",
            data=params.encode(),
            headers=self._get_cookie(),
        )
        res = urllib.request.urlopen(req)
        return res.read().decode()
