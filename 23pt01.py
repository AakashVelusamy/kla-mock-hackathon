
logfile = []
with open('./Milestone1/M1_LogFile.txt', 'r') as f:
    content = f.readlines()
    # print(content)
    for line in content:
        splitline = line.split(']')
        # print(line)
        splitline[0] = splitline[0] + "]"
        splitline[1] = splitline[1].lstrip()
        splitline[1] = splitline[1].rstrip('\n')
        # print(splitline)
        logfile.append(splitline)

    # print(logfile[0])

with open('./Milestone1/M1_CommandFile.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        splitline = line.split(' ', 2)
        # print(splitline)
        splitline[2] = splitline[2].rstrip('\n')
        # print(splitline)
        if(splitline[0] == 'REPLACE'):
            # print(f"OLD: {logfile[int(splitline[1])-1]}")
            logfile[int(splitline[1])-1][1] = splitline[2]
            # print(f"NEW: {logfile[int(splitline[1])-1]}")
# print(logfile)

count_info = 0
count_error = 0
count_warn = 0

for log in logfile:
    splitline = log[1].split(' ', 1)
    # print(splitline)
    if(splitline[0] == 'INFO'):
        count_info += 1
    elif(splitline[0] == 'ERROR'):
        count_error += 1
    elif(splitline[0] == 'WARN'):
        count_warn += 1
    
with open('./Milestone1/M1_ProcessedLogFile.txt', 'w') as f:
    for log in logfile:
        f.write(" ".join(log) + "\n")

with open('./Milestone2/M2_LogFile.txt', 'w') as f:
    for log in logfile:
        f.write(" ".join(log) + "\n")

with open('./Milestone1/M1_Output.txt', 'w') as f:
    f.write(f"INFO: {count_info}\n")
    f.write(f"ERROR: {count_error}\n")
    f.write(f"WARN: {count_warn}\n")

logfile = []
with open('./Milestone2/M2_LogFile.txt', 'r') as f:
    content = f.readlines()
    # print(content)
    for line in content:
        splitline = line.split(']')
        # print(line)
        splitline[0] = splitline[0] + "]"
        splitline[1] = splitline[1].lstrip()
        splitline[1] = splitline[1].rstrip('\n')
        # print(splitline)
        logfile.append(splitline)

    # print(logfile[0])

with open('./Milestone2/M2_CommandFile.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        line = line.rstrip('\n')
        splitline = line.split(' ', 1)
        # print(splitline)
        print(splitline)
        if(splitline[0] == 'INSERT'):
            break
            # insertline[0] = '[' + insertline[0] + ']'
            # print(insertline)
            # logfile.insert(int(splitline[1])-1, insertline)
            # print(logfile[int(splitline[1])-1])
        elif(splitline[0] == 'DELETE'):
            del logfile[int(splitline[1])-1]
# print(logfile)

# with open('./Milestone2/M2_ProcessedLogFile.txt', 'w') as f:
#     for log in logfile:
#         f.write(" ".join(log) + "\n")