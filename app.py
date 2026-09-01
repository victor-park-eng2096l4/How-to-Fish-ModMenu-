# Configuration module: app

SETTINGS = {
    "phwxgw": 379,
    "fpbg": 869,
    "bpzps": 786,
}


def get(key, default=None):
    return SETTINGS.get(key, default)
