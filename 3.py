from getInput import getlines

def doMuls(input):
    total, index, going = 0, 0, True
    while going:
        index = input.find("mul(") + 4
        if index == -1:
            break
        num, num2 = 0, 0
        while True:
            if index >= len(input):
                going = False
                break
            if input[index].isdigit():
                num *= 10
                num += int(input[index])
            elif input[index]==",":
                num2 = num
                num = 0
            elif input[index]==")":
                total += num * num2
                print(num2,"*",num,"=",num*num2)
                num, num2 = 0, 0
                input = input[index + 1:]
                break
            else:
                input = input[index + 1:]
                break
            index += 1
    return total

def part1():
    input = str.join("",getlines(3).split("\n"))
    total = doMuls(input)
    print(total)

def part2():
    input = str.join("",getlines(3).split("\n"))
    dos = input.split("do()")
    new = ""
    for do in dos:
        print(do)
        index = do.find("don't()")
        if index != -1:
            do=do[:index]
        print(do)
        print()
        new += do
    total = doMuls(new)
    print(total)

if __name__ == '__main__':
    part2()