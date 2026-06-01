import pdb
import json

def read_logs():

    # WAY 1
    #file = open("app.log", "r")
    #file.readlines() # operation on file
    #file.close()

    #WAY 2
    line = []
    with open("app.log", "r") as file: #file opened in read mode
        return file.readlines()  #operation on file, file will be automatically closed after this block
        

read_logs()           
def log_analyzer(lines):
   
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

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

def write_report(log_count):
    with open("json_output.json", "w+") as file :
        json.dump(log_count, file)

lines = read_logs()
log_count = log_analyzer(lines)
write_report(log_count)


     