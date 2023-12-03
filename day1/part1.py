
input_text = open("input.txt", "r")
lines = input_text.readlines()
nums = "0123456789"

total = 0

for line in lines:
    lo = 0
    hi = len(line)-1

    while line[lo] not in nums:
        lo += 1

    while line[hi] not in nums:
        hi -= 1

    concat = line[lo] + line[hi]
    total += int(concat)

print(f"Sum is: {total}")    