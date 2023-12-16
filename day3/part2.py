
nums = "0123456789"
symbols = ['/', '*', '=', '%', '@', '&', '-', '+', '$', '#']


def read_file():
    input = open("day3\input.txt", "r")
    lines = input.readlines()

    matrix = []
    for line in lines:
        matrix.append(line)
    return matrix

def get_full_num(line, start_index):
    lo = start_index
    hi = start_index

    while lo > 0 and line[lo-1] != "." and line[lo-1] not in symbols:
        lo -= 1
    while hi < len(line)-1 and line[hi] != "." and line[hi] not in symbols:
        hi += 1
    #print(f"lo: {lo}, hi: {hi}")
    return line[lo:hi]

def get_surrounding(matrix, i, j):
    numbers = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            new_y = min(max(0, i + y), len(matrix))
            new_x = min(max(0, j + x), len(matrix[i].strip())) 
            if matrix[new_y][new_x] in nums:
                num = get_full_num(matrix[new_y], new_x)
                if num not in numbers:
                    numbers.append(num)
                #print(f"Found: {matrix[new_y][new_x]} at y: {new_y}, x: {new_x}, returned: {num}")
    #print(numbers)
    return numbers

def main():
    matrix = read_file()
    print(f"Matrix height: {len(matrix)} \nMatrix length: {len(matrix[0].strip())}" )
    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "*":
                nums = get_surrounding(matrix, i , j)
                if len(nums) == 2:
                    total += (int(nums[0]) * int(nums[1]))

    print(total)
    

if __name__ == "__main__":
    main()