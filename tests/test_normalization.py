import pytest
from ChemnameNormalizer import Normalizer


@pytest.mark.asyncio
@pytest.mark.parametrize("names, expected",
     [
         (["aden0card", "Adenocard", "BG8967", "N0NEX1STENT", "BAYT006267", "diflucan", "ibrut1nlb", "PC-32765"],
          ["adenosine", "adenosine", "bivalirudin", None, "fluconazole", "fluconazole", "ibrutinib", "ibrutinib"])
     ])
def test_normalize(names, expected):
    app = Normalizer(format="trivial")
    result = app.normalize(names)

    assert result == expected
