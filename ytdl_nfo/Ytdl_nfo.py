import os
import json
import nfo

class Ytdl_nfo:
    def __init__(self, file_path):
        self.path = file_path
        self.filename = os.path.splitext(file_path)[0]

        # Read json data
        with open(self.path, 'r') as f:
            self.data = json.load(f)
        self.extractor = self.data['extractor'].lower()
        self.nfo = nfo.get_config(self.extractor)

    def process(self):
        self.nfo.generate(self.data)
        self.nfo.print_nfo()
        self.nfo.write_nfo(f'{self.filename}.nfo')

    def print_data(self):
        print(json.dumps(self.data, indent=4, sort_keys=True))

