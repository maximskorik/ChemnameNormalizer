from .pubchemapi import _PubChemAPI

import asyncio
from aiohttp import ClientSession
from typing import List


class Normalizer:

    def __init__(self, format: str = "trivial"):
        self.normalization_format = format
        self.original_names = None
        self.norm_names = None

    def normalize(self, names: List) -> List[str]:
        self.original_names = names
        asyncio.run(self._run_query(names))
        self.norm_names = self._format_names(self.norm_names)
        return self.norm_names

    async def _run_query(self, names: List):
        async with ClientSession() as session:
            api = _PubChemAPI(session=session, normalization_format=self.normalization_format)
            norm_names = [await api.get_name(name) for name in names]
        self.norm_names = norm_names

    @staticmethod
    def _format_names(names: List) -> List[str]:
        names = [name.lower() if type(name) is str else name for name in names]
        return names
