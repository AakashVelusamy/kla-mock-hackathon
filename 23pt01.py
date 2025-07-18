import datetime 

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
        if(splitline[0] == 'INSERT'):
            timesplit = splitline[1].split(']')[0]
            timesplit = timesplit.lstrip('[')
            # print(timesplit)
            i = 0
            format_string = "%Y-%m-%d %H:%M:%S"
            for log in logfile:
                # print(log)
                x = log[0].lstrip('[')
                x = x.rstrip(']')
                # print(x)
                # print(timesplit)
                # print(log[0])
                logdate =  datetime.datetime.strptime(x, format_string)
                insertdate = datetime.datetime.strptime(timesplit, format_string)
                if(logdate < insertdate):
                    break
                else:
                    i += 1
            splitline = line.split(']')
            splitline[0] = splitline[0].split(' ', 1)[1]
            # print(splitline[0])
            splitline[0] = splitline[0] + "]"
            splitline[1] = splitline[1].lstrip()
            splitline[1] = splitline[1].rstrip('\n')
            # print(splitline)
            logfile.insert(i, splitline)
            # print(logfile[i])
        elif(splitline[0] == 'DELETE'):
            del logfile[int(splitline[1])-1]
# print(logfile)

counts = {}
for log in logfile:
    if log[1].count('logged in'):
        start = log[1].find("'")
        end = log[1].find("'", start + 1)
        username = log[1][start+1:end]
        # print(username)
        if username in counts:
            counts[username] += 1
        else:
            counts[username] = 1

with open('./Milestone2/M2_ProcessedLogFile.txt', 'w') as f:
    for log in logfile:
        f.write(" ".join(log) + "\n")

with open('./Milestone2/M2_Output.txt', 'w') as f:
    for username, count in counts.items():
        f.write(f"{username}: {count}\n")

logfile1 = []
logfile2 = []

with open('./Milestone3/M3_LogFile1.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        splitline = line.split(']')
        splitline[0] = splitline[0] + "]"
        splitline[1] = splitline[1].lstrip()
        splitline[1] = splitline[1].rstrip('\n')
        logfile1.append(splitline)

with open('./Milestone3/M3_LogFile2.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        splitline = line.split(']')
        splitline[0] = splitline[0] + "]"
        splitline[1] = splitline[1].lstrip()
        splitline[1] = splitline[1].rstrip('\n')
        logfile2.append(splitline)

commands = []
i = 0
j = 0
format_string = "%Y-%m-%d %H:%M:%S"

while i < len(logfile1) and j < len(logfile2):
    log1_time = logfile1[i][0].lstrip('[').rstrip(']')
    log2_time = logfile2[j][0].lstrip('[').rstrip(']')
    log1_date = datetime.datetime.strptime(log1_time, format_string)
    log2_date = datetime.datetime.strptime(log2_time, format_string)
    logfile2[j][1] = logfile2[j][1].replace('  ', ' ')
    if logfile1[i] == logfile2[j]:
        i += 1
        j += 1
    else:
        if log1_date == log2_date:
            commands.append(f"REPLACE {i+1} {logfile2[j][1]}")
            i += 1
            j += 1
        elif log1_date < log2_date:
            commands.append(f"DELETE {i+1}")
            i += 1
        else:
            commands.append(f"INSERT [{log2_time}] {logfile2[j][1]}")
            j += 1

while i < len(logfile1):
    commands.append(f"DELETE {i+1}")
    i += 1

while j < len(logfile2):
    log2_time = logfile2[j][0].lstrip('[').rstrip(']')
    logfile2[j][1] = logfile2[j][1].replace('  ', ' ')
    commands.append(f"INSERT [{log2_time}] {logfile2[j][1]}")
    j += 1

with open('./Milestone3/M3_Output.txt', 'w') as f:
    for command in commands:
        f.write(command + "\n")

