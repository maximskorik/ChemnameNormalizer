from aiohttp import ClientSession
import pytest
from CompoundsNormalizer.pubchemapi import _PubChemAPI


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,norm_format,expected",
    [("Adenocard", "trivial", "adenosine"),
     ("diflucan", "trivial", "fluconazole"),
     ("BAYT006267", "trivial", "fluconazole"),
     ("N0NEX1STENT", "trivial", None),
     ("Adenocard", "iupac", "(2R,3R,4S,5R)-2-(6-aminopurin-9-yl)-5-(hydroxymethyl)oxolane-3,4-diol"),
     ("diflucan", "iupac", "2-(2,4-difluorophenyl)-1,3-bis(1,2,4-triazol-1-yl)propan-2-ol"),
     ("BAYT006267", "iupac", "2-(2,4-difluorophenyl)-1,3-bis(1,2,4-triazol-1-yl)propan-2-ol"),
     ("N0NEX1STENT", "iupac", None),
     ("aden0card", "trivial", "adenosine")
     ]
)
async def test_get_name(name, norm_format, expected):
    async with ClientSession() as session:
        api = _PubChemAPI(session=session, normalization_format=norm_format)
        name = await api.get_name(name)

    assert name == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name, expected",
    [("aden0card", "Adenocard"),
     ("d1flucan", "Diflucan"),
     ("asripin", "aspirin"),
     ("fluoconazolle", "fluconazole"),
     ("n0nex1stent", None)
     ]
)
async def test_fuzzy_search_name(name, expected):
    async with ClientSession() as session:
        api = _PubChemAPI(session=session, normalization_format="trivial")
        name = await api.fuzzy_search_name(name)

    assert name == expected
