from getInput import getlines

SEARCH = "XMAS"

def move(i,j,direction):
    if direction.contains("N"):
        i -= 1
    if direction.contains("E"):
        j += 1
    if direction.contains("S"):
        i += 1
    if direction.contains("W"):
        j -= 1
    return i, j

def get(list, i, j):
    return list[i][j]

def equals(letter, word, num, list, i, j, dir):
    if word[num] == letter:
        if num == len(word) - 1:
            return True
        return equals(get(list, move(i, j, dir)), word, num+1, list, move(i, j, dir), dir)
    else:
        return False

def findLetters(crossword, letter):
    found = []
    for i, line in enumerate(crossword):
        for j, l in enumerate(line):
            if l == letter:
                found.append([i, j])
    return found

def part1():
    letters = []
    lines = getlines(4).split("\n")
    xmasCount = 0
    for line in lines:
        letters.append(list(line))# accest to characters by row and collumn indexing
    for cords in findLetters(letters, SEARCH[0]):
        i, j = cords
        if equals(get(letters, move(i, j, "N")), SEARCH, 1, letters, move(i, j), dir):
            xmasCount += 1
    print(xmasCount)


        

if __name__ == '__main__':
    part1()