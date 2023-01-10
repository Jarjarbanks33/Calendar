days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print("January 2023")
days_line = ""

def printDateLine(start, late):
    line = ""
    for i in range(start, late):
        line += str(i) + "\t"
    print(line)


for i in range(0, 7):
    days_line += days[i]+"\t"
print(days_line)

printDateLine(1, 8)
printDateLine(8, 15)
printDateLine(15, 22)
printDateLine(22, 28)
printDateLine(28, 32)