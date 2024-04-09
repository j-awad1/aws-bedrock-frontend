import csv
import os


class Logger:
    def __init__(self):
        # user = input("ENTER NAME FOR LOGGING: ")
        # self.user = user
        self.file_Llama = "Log_Llama.csv"
        self.file_Clause2 = "Log_Claude_2.csv"
        # self.file_Clause3 = "Log_Claude_3.csv"
        self.init_CSV(self.file_Llama)
        self.init_CSV(self.file_Clause2)
        # self.init_CSV(self.file_Clause3)
        
    #create CSV files and add rows
    def init_CSV(self, filename):
        if not os.path.isfile(filename):
            file = open(filename, 'w', newline='')
            writer = csv.DictWriter(file, ["Model", "TimeStamp", "Input Prompt", "Max Generation Length", "Temperature", "Top_P", "Response"])
            writer.writeheader()
            
        else:
            print(f'Using Existing {filename} Log File')
     
    #Log data given a variable
    def log_data(self, modelName, data):
        
        if modelName == "Llama2_13B":
            fileName = self.file_Llama
        if modelName == "Claude2v1":
            fileName = self.file_Clause2
            
            
        with open(fileName, 'r', newline='') as file:
            reader = csv.DictReader(file)
            fields = list(reader)
           
        # header = rows[0].keys() #takes only column names
        
        # rows[0][rowName] = data
        # print('Temperature value: ', rows[0][rowName])
        # print("header" ,header)
#         row_index = [row[header[0]] for row in rows[1:]].index(rowName) + 1
        print(data)
        
#         print("row index" ,row_index)
        with open(fileName, 'a',  newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        
                     
# if __name__ == "__main__":
#     logger = Logger()
#     data = [logger.user, "iput", 2, .1, .5, "response"]
#     logger.log_data("Llama", 'Temperature', data)
        