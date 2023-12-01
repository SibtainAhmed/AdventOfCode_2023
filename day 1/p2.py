file = open('day 1/p2.txt')
digits = { 'one':'1', 'two':'2', 'three':'3', "four":'4', "five":'5', "six":'6', 'seven':'7', "eight":'8', 'nine':'9'}
def solve():
    f = s = 0
    S = file.readline().strip()
    index = -1
    for val in S:
        index += 1
        if val.isnumeric():
            f = val
            break
        elif val not in ('o', 't', 'f', 's', 'e', 'n'):
            continue
        elif S[index:index+3] in digits:
            f = digits[S[index:index+3]]
            break
        elif S[index:index+4] in digits:
            f = digits[S[index:index+4]]
            break
        elif S[index:index+5] in digits:
            f = digits[S[index:index+5]]
            break

    for index in range(len(S)-1, -1, -1):
        val = S[index]
        if val.isnumeric():
            s = val
            break
        elif val not in ('o', 't', 'f', 's', 'e', 'n'):
            continue
        elif S[index:index+3] in digits:
            s = digits[S[index:index+3]]
            break
        elif S[index:index+4] in digits:
            s = digits[S[index:index+4]]
            break
        elif S[index:index+5] in digits:
            s = digits[S[index:index+5]]
            break
    return int(f+s)




val = 0
for i in range(1000):
    val += solve()
    print(val)

print(val)
# return val



file.close()
