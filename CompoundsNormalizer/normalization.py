from typing import List


class Normalizer:

    def __init__(self, normalization_format: str = "iupac"):
        self._format = normalization_format

    def normalize(self, *args) -> List[str]:
        pass
