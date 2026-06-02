import pdb
import json

class LogAnalyzer: # Class Creation here
        
        # class has 2 things : 1. data members (variables) 2. member functions (methods)
        def __init__(self, input_file, output_file): #It is like constructor
            self.input_file = input_file
            self.output_file = output_file

        def read_logs(self):

        # WAY 1
        #file = open("app.log", "r")
        #file.readlines() # operation on file
        #file.close()
        

        #WAY 2
        
           with open(self.input_file, "r") as file: #file opened in read mode
            return file.readlines()  #operation on file, file will be automatically closed after this block
                       
        def log_analyzer(self):
        
            log_count = {
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0
            }
             
            lines = self.read_logs() # method calling inside class 

            for line in lines:
                if "INFO" in line:
                    log_count["INFO"] += 1 # log_count.update({"INFO": log_count["INFO"] + 1})
                elif "WARNING" in line:
                    log_count["WARNING"] += 1
                elif "ERROR" in line:
                    log_count["ERROR"] += 1
                else :
                    pass    
            
            print(log_count)
            return log_count

        def write_report(self, log_count):
         with open(self.output_file, "w+") as file :
            json.dump(log_count, file)

obj1 = LogAnalyzer("app.log", "json_outputzz.json") # object creation
obj2 = LogAnalyzer("app2.log", "json_output2.json") # object creation


log_count = obj1.log_analyzer()
obj1.write_report(log_count)

log_count2 = obj2.log_analyzer()
obj2.write_report(log_count2)


     