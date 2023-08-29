import csv

class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)  # Skip the header row
            data = [row for row in reader]
        return headers, data
