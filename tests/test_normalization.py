import pytest
from CompoundsNormalizer.normalization import CompoundNameNormalizer


def test_normalize_to_trivial():
    input = ["Adenosine", "Adenocard", "BG8967", "Bivalirudin", "BAYT006267", "diflucan", "ibrutinib", "PC-32765"]
    expected = ["adenosine", "adenosine", "bivalirudin", "bivalirudin", "fluconazole", "fluconazole", "ibrutinib",
                "ibrutinib"]

    actual = CompoundNameNormalizer(input).normalize(type="common")
    assert actual == expected


@pytest.mark.skip(reason="Missing expected data")
def test_normalize_to_iupac():
    input = ["Adenosine", "Adenocard", "BG8967", "Bivalirudin", "BAYT006267", "diflucan", "ibrutinib", "PC-32765"]
    expected = []  # TODO

    actual = CompoundNameNormalizer(input).normalize(type="iupac")
    assert actual.normalized_names == expected
