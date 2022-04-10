from aiohttp import ClientSession


class _PubChemAPI:

    _url_prefixes = {"search": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name",
                     "fuzzy_search": "https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/compound"}
    _url_suffixes = {"trivial": "synonyms",
                     "iupac": "property/iupacname"}

    def __init__(self, session: ClientSession, normalization_format: str):
        self._format = normalization_format
        self._session = session

    async def get_name(self, name: str):
        if name is None:
            return None
        url = self._construct_url(name)
        response = await self._query_server(url)
        if self._request_is_ok(response.status):
            return await self._parse_response(response)
        else:
            return await self.get_name(
                await self.fuzzy_search_name(name))

    async def fuzzy_search_name(self, name: str):
        url = self._construct_url(name, "fuzzy_search")
        response = await self._query_server(url)
        return await self._parse_fuzzy_response(response)

    async def _parse_response(self, response):
        data = await response.json()
        if self._format == "trivial":
            return data["InformationList"]["Information"][0]["Synonym"][0]
        else:
            return data["PropertyTable"]["Properties"][0]["IUPACName"]

    @staticmethod
    async def _parse_fuzzy_response(response):
        data = await response.json()
        try:
            return data.get("dictionary_terms", None).get("compound")[0]
        except AttributeError:
            return None

    async def _query_server(self, url: str):
        response = await self._session.get(url)
        return response

    def _construct_url(self, name: str, prefix: str = "search"):
        name = name.replace(" ", "%20")
        prefix_url = self._url_prefixes[prefix]
        suffix = self._url_suffixes[self._format]
        url = "/".join([prefix_url, name])
        if prefix == "search":
            url += "/" + suffix
        return url + "/json"

    @staticmethod
    def _request_is_ok(response: int):
        return response == 200
