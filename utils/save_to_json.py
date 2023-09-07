import json
from .util import *



def save_stats_json(statistic: dict, folder: str, filename: str):
    path = basic_operation(folder, filename)

    with open(path, 'w') as outfile:
        json.dump(statistic, outfile, indent=4, sort_keys=False)
