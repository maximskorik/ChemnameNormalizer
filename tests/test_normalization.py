import pytest
from CompoundsNormalizer import Normalizer


@pytest.mark.asyncio
@pytest.mark.parametrize("names, expected",
     [
         (["aden0card", "Adenocard", "BG8967", "N0NEX1STENT", "BAYT006267", "diflucan", "ibrut1nlb", "PC-32765"],
          ["adenosine", "adenosine", "bivalirudin", None, "fluconazole", "fluconazole", "ibrutinib", "ibrutinib"])
     ])
async def test_normalize(names, expected):
    app = Normalizer()
    result = await app.normalize(names, "trivial")

    assert result == expected


@pytest.mark.skip(reason="Not implemented")
def test_read_names_from_file():
    pass
