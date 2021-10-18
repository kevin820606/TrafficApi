from logging import INFO, FileHandler, Formatter, Logger, getLogger
from datetime import datetime
from dataclasses import dataclass, fields

# https://stackoverflow.com/a/62750694/10574593
def create_logger() -> Logger:

    logger = getLogger(__name__)
    logger.setLevel(INFO)
    formatter = Formatter("[%(asctime)s| %(levelname)s| %(processName)s] %(message)s")
    handler = FileHandler(f"logs/{__name__}.log")
    handler.setFormatter(formatter)

    # this bit will make sure you won't have
    # duplicated messages in the output
    if not len(logger.handlers):
        logger.addHandler(handler)
    return logger


@dataclass
class trafficapidata:
    __slots__ = [
        "region",
        "srcdetail",
        "areaNm",
        "UID",
        "direction",
        "y1",
        "happentime",
        "roadtype",
        "road",
        "modDttm",
        "comment",
        "happendate",
        "x1",
    ]
    region: str
    srcdetail: str
    areaNm: str
    UID: str
    direction: str
    y1: float
    happentime: str
    roadtype: str
    road: str
    modDttm: datetime
    comment: str
    happendate: str
    x1: float

    def __post_init__(self):
        self.modDttm = datetime.strptime(self.modDttm, "%Y-%m-%d %H:%M:%S.%f")
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                setattr(self, field.name, field.type(value))
