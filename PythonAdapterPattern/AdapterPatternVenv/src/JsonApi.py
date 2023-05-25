import json

from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IJsonFile


class JsonApi(IJsonFile):

    def __init__(self):
        self.file = None

    def print_json_file(self, element_name, filename):
        print(self.load_json_file(filename))

    def find_element_in_json(self, element):
        results = []

        def search_json(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == element:
                        results.append(value)
                    else:
                        search_json(value)
            elif isinstance(data, list):
                for item in data:
                    search_json(item)

            search_json(self.file)
            return results

    def load_json_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.file = data
