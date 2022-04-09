import asyncio
import pytest
from CompoundsNormalizer import Normalizer


@pytest.mark.asyncio
@pytest.mark.parametrize("names, expected",
     [
         (["Adenosine", "Adenocard", "BG8967", "NONEXISTENT", "BAYT006267", "diflucan", "ibrutinib", "PC-32765"],
          ["adenosine", "adenosine", "bivalirudin", None, "fluconazole", "fluconazole", "ibrutinib", "ibrutinib"])
     ])
async def test_normalize(names, expected):
    app = Normalizer()
    result = await app.normalize(names, "trivial")

    assert result == expected
