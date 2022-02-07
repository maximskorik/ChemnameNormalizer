from CompoundsNormalizer import CompoundNameNormalizer

if __name__ == "__main__":
    compounds = ["Adenosine", "Adenocard", "BG8967", "Bivalirudin", "BAYT006267", "diflucan", "ibrutinib", "PC-32765"]
    normalizer = CompoundNameNormalizer(compounds)
    normalizer.normalize()
    print(normalizer.as_pandas())
