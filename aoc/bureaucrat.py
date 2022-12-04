from pathlib import Path


class Stenographer:
    def __init__(self) -> None:
        self.data_dir = Path.cwd() / "data"

    @property
    def _check_dir(self):
        return self.data_dir.exists()

    @property
    def _create_data_dir(self):
        Path.mkdir(self.data_dir, parents=True, exist_ok=True)

    def record(self, data, year, day):
        if not self._check_dir:
            self._create_data_dir

        filename = f"year_{year}_day_{day}.txt"
        with open(f"data/{filename}", "w") as f:
            f.write(data)
