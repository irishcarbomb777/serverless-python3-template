import sys
import json
import argparse


def parseLocalEvent(event):
    try:
        if sys.argv[1]:

            print("test1")
            parser = argparse.ArgumentParser()
            parser.add_argument('--infile', nargs=1,
                        help="JSON file to be processed",
                        type=argparse.FileType('r'))
            arguments = parser.parse_args()
            # Loading a JSON object returns a dict.
            event = json.load(arguments.infile[0])
            return event
    except:
        return event
    