

from dataclasses import replace
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

def test():
    s1 = "Game 1: 1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green"
    new_s1 = format(s1)
    a = get_maxed_used_color(new_s1, "blue")
    print(a)


def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    total = 0  # The sum of all game numbers that are possible

    for index, line in enumerate(lines):
        formatted = format(line)
        if check(formatted):
            total += index + 1

    print(f"Total: {total}")


        


if __name__ == "__main__":
    main()