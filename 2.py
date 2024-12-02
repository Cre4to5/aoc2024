from getInput import getlines

def part1():
    lines = getlines(2)
    safe = 0
    for line in lines:
        cont = False
        changes = []
        numbers = [int(x.strip()) for x in str.split(line," ")]
        for i in range(len(numbers) - 1):
            change = numbers[i] - numbers[i + 1]
            changes.append(change)
            if abs(change) < 1 or abs(change) > 3:
                cont = True
        for i in range(len(changes) - 1):
            if (changes[i] > 0) != (changes[i + 1] > 0):
                cont = True
        if cont == True:
            continue
        safe += 1
    print(safe)

if __name__ == '__main__':
    part1()