import requests
from requests.exceptions import HTTPError


class APIquery:
    def __init__(self) -> None:
        self.url = "https://od.moi.gov.tw/MOI/v1/pbs/"

    def _get_data(self) -> list[dict]:

        req = requests.get(self.url)
        return req.json()

    def _data_parse(self):
        self.json = self._get_data()
