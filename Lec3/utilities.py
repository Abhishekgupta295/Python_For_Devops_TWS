import json

# package are the function which can be called in other files

def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()


def write_json(filename, json_object):
    with open(filename, "w+") as file:
        json.dump(json_object, file)