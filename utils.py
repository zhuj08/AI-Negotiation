import sys  
import os
import re
import json

import numpy


def fileToList(filepath):
    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    lines = [line.rstrip('\n') for line in open(filepath)]
    return lines