file = open('day 2/p1.txt')
limits = {'red':12, 'green':13, 'blue':14}

def solve(line):
    colorString = line.strip().split(':')[1]  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    handfulColorList = colorString.strip().split(';') # ['3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
    for j in handfulColorList:
        colorPairList = j.strip().split(',') # ['3 blue', ' 4 red']
        for k in colorPairList:
            value, color = k.strip().split(' ')
            if int(value) > limits[color]:
                return False
    return True 



allTestCases = file.readlines()

val = 0
for i in range(1, 1 + len(allTestCases)):
    if solve(allTestCases[i-1]):
        val += i
        print('value', val)

print(val)



file.close()
