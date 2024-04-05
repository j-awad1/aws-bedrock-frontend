import csv
import os


class Logger:
    def __init__(self):
        self.file_M1 = "Log_Llama.csv"
        self.file_M2 = "Log_Claude.csv"
        self.init_CSV(self.file_M1)
        self.init_CSV(self.file_M2)
        
    def init_CSV(self, filename):
        if not os.path.isfile(filename):
            file = open(filename, 'w', newline='')
            writer = csv.DictWriter(file, ["Input Prompt", "Response", "Max Generation Length", "Temperature", "Top_P"])
            writer.writeheader()
        else:
            print(f'Using Existing {filename} Log')
        
    def log_data(self, data):
        file = open(filename, 'a', newline='')
        
        
Logger()
        