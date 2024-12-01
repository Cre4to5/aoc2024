from getInput import getlines

def part1():
        lines = getlines(1)
        list1 = []
        list2 = []
        for line in lines:
            twonums = line.strip().split("   ")
            list1.append(int(twonums[0]))
            list2.append(int(twonums[1]))
        list1.sort()
        list2.sort()
        totaldist = 0
        for num1, num2 in zip(list1, list2):
            totaldist += abs(num1-num2)
        print(totaldist)

def part2():
        lines = getlines(1)
        list1 = []
        list2 = []
        for line in lines:
            twonums = line.strip().split("   ")
            list1.append(int(twonums[0]))
            list2.append(int(twonums[1]))
        list1.sort()
        list2.sort()
        similarity = 0
        for num1 in list1:
            similarity += list2.count(num1) * num1
        print(similarity)

if __name__ == '__main__':
    part2()