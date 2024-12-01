
def part1():
    with open("./inputs/1.txt", "r")as f:
        lines = f.readlines()
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

def main():
    part1()

if __name__ == '__main__':
    main()