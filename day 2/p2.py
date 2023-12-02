file = open('day 2/puzzle.txt')

def solve(line):
    maxColorValue = {'red':0, 'green':0, 'blue':0}
    colorString = line.strip().split(':')[1]  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    handfulColorList = colorString.strip().split(';') # ['3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
    for j in handfulColorList:
        colorPairList = j.strip().split(',') # ['3 blue', ' 4 red']
        for k in colorPairList:
            value, color = k.strip().split(' ')
            if int(value) > maxColorValue[color]:
                maxColorValue[color] = int(value)
    return maxColorValue['red']*maxColorValue['green']*maxColorValue['blue'] 



allTestCases = file.readlines()

val = 0
for i in range(1, 1 + len(allTestCases)):
    val += solve(allTestCases[i-1])
    # print('value', val)

print(val)



file.close()
