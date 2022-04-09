from aiohttp import ClientSession


class PubChemAPI:

    _url_suffixes = {"trivial": "synonyms/json",
                     "iupac": "property/iupacname/json"}

    def __init__(self, session: ClientSession, normalization_format: str):
        self._format = normalization_format
        self._session = session

    async def get_name(self, name: str):
        url = self._construct_url(name)
        response = await self._query_server(url)
        if self._request_is_ok(response.status):
            return await self._parse_response(response)
        else:
            return None

    async def _parse_response(self, response):
        data = await response.json()
        if self._format == "trivial":
            return data["InformationList"]["Information"][0]["Synonym"][0]
        else:
            return data["PropertyTable"]["Properties"][0]["IUPACName"]

    async def _query_server(self, url: str):
        response = await self._session.get(url)
        return response

    def _construct_url(self, name: str):
        prefix = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name"
        suffix = self._url_suffixes[self._format]
        url = "/".join([prefix, name, suffix])
        return url

    @staticmethod
    def _request_is_ok(response: int):
        return response == 200

