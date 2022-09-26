import json

class OpenJson:
    @staticmethod
    def get_json():
        with open('config.json', 'r') as f:
            data = json.load(f)
            return data