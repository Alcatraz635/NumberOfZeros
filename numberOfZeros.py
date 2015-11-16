import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')

def compZeros(zeroOccurences, number):
    counter = 0
    binNum = lambda x: x >= 0 and int(str(bin(x))[2:])
    for num in range(1, number+1):
        countList = Counter(list(str(binNum(num))))
        if countList['0'] == zeroOccurences: counter+=1
    return counter

for test in test_cases:
    test = test.strip().split(" ")
    print compZeros(int(test[0]), int(test[1]))

test_cases.close()
exit(0)