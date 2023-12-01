file = open('day 1/p1.txt')

def solve():
    f = s = 0
    S = file.readline().strip()
    for i in S:
        if i.isnumeric():
            f = i
            break
    for i in S[::-1]:
        if i.isnumeric():
            s = i
            break
    return int(f+s)



# noOfTestCases = file.readline()
# print(noOfTestCases)

val = 0
for i in range(1000):
    val += solve()
    print(val)

print(val)
# return val



file.close()
