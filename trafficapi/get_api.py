import requests
from utils import trafficapidata


class APIquery:
    def __init__(self) -> None:
        self.url = "https://od.moi.gov.tw/MOI/v1/pbs/"
        self.data: dict[str, trafficapidata] = dict()

    def __get_data(self) -> list[dict]:
        req = requests.get(self.url)
        return req.json()

    def __data_parse(self):
        apidata = self.__get_data()
        for apidatum in apidata:
            self.data |= {apidatum["UID"]: trafficapidata(**apidatum)}

    def run(self):
        self.__data_parse()
