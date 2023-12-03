import math


def format(s: str) -> list[str]:
    i = s.index(":")
    new_s = s[i+1::].replace(" ", "").replace(";", ",")
    new_s = list(new_s.split(","))
    return new_s


def get_maxed_used_color(arr, keyword):
    new_arr = []
    for i in arr:
        current = i
        if keyword in i:
            new_arr.append(int(current.replace(keyword, "")))
    return max(new_arr)


def check(arr):
    num_reds = 12
    num_greens = 13
    num_blues = 14

    max_reds = get_maxed_used_color(arr, "red")
    max_greens = get_maxed_used_color(arr, "green")
    max_blues = get_maxed_used_color(arr, "blue")

    if max_reds > num_reds or max_greens > num_greens or max_blues > num_blues:
        return False
    return True

def get_powers(arr):

    max_reds = get_maxed_used_color(arr, "red")
    max_greens = get_maxed_used_color(arr, "green")
    max_blues = get_maxed_used_color(arr, "blue")
    #print(f"red: {max_reds}, green: {max_greens}, blue: {max_blues}")

    return max_reds * max_greens * max_blues

def test():
    file = open("input_test.txt", "r")
    lines = file.readlines()

    total = 0  

    for line in lines:
        formatted = format(line)
        total += get_powers(formatted)

def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    total = 0  

    for index, line in enumerate(lines):
        formatted = format(line)
        total += get_powers(formatted)

    print(f"Total: {total}")


        


if __name__ == "__main__":
    main()