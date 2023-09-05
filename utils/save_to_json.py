import json
from .util import *



def save_stats_json(statistic, folder, filename):
    path = basic_operation(folder, filename)

    with open(path, 'w') as outfile:
        json.dump(statistic, outfile, indent=4, sort_keys=True)
