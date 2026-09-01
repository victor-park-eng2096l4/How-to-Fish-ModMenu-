# Configuration module: loader

SETTINGS = {
    "nwcodx": 292,
    "fphtu": 727,
    "hkxwgv": 103,
    "tdghfc": 773,
    "hihiu": 59,
}


def get(key, default=None):
    return SETTINGS.get(key, default)
