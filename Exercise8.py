import sys
a = sys.argv[1]
with open(a,'r+') as file:
    command = sys.argv[2]
    command=command.split(",")
    Data = []
    Value = []
    for line in file:
        line = line.rstrip("\n")
        line = line.split(":")
        Data.append(line[0])
        Value.append(line[1])
    Data = dict(zip(Data,Value))
    for commands in command:
        try:
            print(f"Name:{commands},University:{Data[commands]}")
        except:
            print(f"No record of {commands} was found")