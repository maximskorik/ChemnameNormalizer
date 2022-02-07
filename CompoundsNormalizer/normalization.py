from typing import List
from pubchempy import get_compounds
import pandas


class CompoundNameNormalizer:

    def __init__(self, compound_names: List[str]):
        self.mapper = {"common": self.to_common,
                       "iupac": self.to_iupac}
        self.original_names = compound_names
        self.normalized_names = None

    def normalize(self, type="common") -> List[str]:
        self.normalized_names = []
        for name in self.original_names:
            self.normalized_names.append(self.mapper[type](name))
        return self.normalized_names

    @staticmethod
    def to_common(name: str) -> str:
        compound = get_compounds(name, "name")[0]
        return compound.synonyms[0].lower()

    @staticmethod
    def to_iupac(name: str) -> str:
        compound = get_compounds(name, "name")[0]
        return compound.iupac_name.lower()

    def as_pandas(self) -> pandas.DataFrame:
        if self.normalized_names is None:
            print("Normalization has not been performed yet.")
        else:
            return pandas.DataFrame({"org_form": self.original_names,
                                     "normed_form": self.normalized_names})
