
def SearchStatusSubtype(statusName):
    message = ""
    if statusName in f:
        parts = f.split(statusName)
        message = parts[1].strip()
    return message

#open file, read only (python default is rt)
#"with" will close the file automatically
fileContent = " "
try:
    with open("sample.log", "r") as file:
        fileContent = file.readlines() #returns a list of lines
except FileNotFoundError:
    print("File does not exist")

#read file line by line
#check for types of error and count its error
# INFO, WARNING, ERROR
infoCount = 0
warningCount = 0
errorCount = 0
for f in fileContent:
    if "INFO" in f:
        infoCount += 1
    elif "WARNING" in f:
        warningCount += 1
    elif "ERROR" in f:
        errorCount += 1
    else:
        print("File is Wrong")


info_messages = []
error_messages = []
warning_messages = []

for f in fileContent:
    tmp = SearchStatusSubtype("INFO")
    if tmp != "":
        info_messages.append(tmp)
    tmp = SearchStatusSubtype("ERROR")
    if tmp != "":
        error_messages.append(tmp)
    tmp = SearchStatusSubtype("WARNING")
    if tmp != "":
        warning_messages.append(tmp)
print("The following is the ERROR")


errorSummary = {} #list
for msg in error_messages:
    errType = msg.split(" ", 1) #split the message into 2 parts
    if errType[0] in errorSummary: #err[0] is the error type we want
        errorSummary[errType[0]] += 1
    else:
        errorSummary[errType[0]] = 1


 
print("\n--- Log Summary ---")
print("Info:", infoCount, "|", "Warning:", warningCount, "|", "Error:", errorCount)
print("\nTop Errors:")
for msg, count in errorSummary.items():
    print(f"{msg}: {count}")


