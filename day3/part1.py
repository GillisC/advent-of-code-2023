nums = ["0123456789"]

def read_file():
    input = open("input_test.txt", "r")
    lines = input.readlines()

    matrix = []
    for line in lines:
        matrix.append(line)
    return matrix

def get_full_number(input, y, x):
    lo = x
    hi = x
    while input[y][lo] in nums and lo >= 0:
        if lo == 0 and input[y][lo] in nums:
            start = lo
            break
        lo -= 1
    start = lo + 1

    while input[y][hi] in nums and hi < len(input):
        if lo == len(input)-1 and input[y][hi] in nums:
            end = hi+1
            break
        hi+=1
    end = hi
    print(input[y][start:end])
    return input[y][start:end]

        
            

def get_adjacent(input, y, x):
    print(f"y: {y}, x: {x}")
    for i in range(-1, 2):
        if y-1 >= 0 and x+i >= 0 and x+i < len(input[y]) and input[y-1][x+i] in nums:
            print(get_full_number(input, y-1, x+i))
    for i in range(-1, 2):
        if y >= 0 and x+i >= 0 and x+i < len(input[y]) and input[y][x+i] in nums:
            print(get_full_number(input, y, x+i))
    for i in range(-1, 2):
        if y+1 >= 0 and y+1 < len(input) and x+i >= 0 and x+i < len(input[y]) and input[y+1][x+i] in nums:
            print(get_full_number(input, y+1, x+i))

            



def main():
    input = read_file()
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] not in nums and input[i][j] != ".":
                get_adjacent(input, i, j)


if __name__ == "__main__":
    main()