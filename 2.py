from getInput import getlines

def isUnsafe(numbers):
    changes = []
    for i in range(len(numbers) - 1):
        change = numbers[i] - numbers[i + 1]
        changes.append(change)
        if abs(change) < 1 or abs(change) > 3:
            return True
    for i in range(len(changes) - 1):
        if (changes[i] > 0) != (changes[i + 1] > 0):
            return True
    return False

def part1():
    lines = getlines(2).split("\n")
    safe = 0
    for line in lines:
        numbers = [int(x.strip()) for x in str.split(line," ")]
        if isUnsafe(numbers):
            continue
        safe += 1
    print(safe)

def listWithout(list, i):
    return list[:i] + list[(i + 1):]

def isSafeAnyway(list):
    for i in range(len(list)):
        if not isUnsafe(listWithout(list,i)):
             return True
    return False

def part2():
    lines = getlines(2).split("\n")
    safe = 0
    for line in lines:
        numbers = [int(x.strip()) for x in str.split(line," ")]
        cont = False
        if isUnsafe(numbers):
            if isSafeAnyway(numbers):
                safe += 1
        else:
            safe += 1
    print(safe)

if __name__ == '__main__':
    part2()